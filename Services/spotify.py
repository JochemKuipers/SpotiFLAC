import spotipy
import spotipy.oauth2
from PyQt6.QtCore import QThread, pyqtSignal
import math
from concurrent.futures import ThreadPoolExecutor, as_completed


class TrackFetchWorker(QThread):
    """Worker thread for fetching a batch of tracks at a specific offset"""

    finished = pyqtSignal(list, int)  # tracks, offset
    error = pyqtSignal(str, int)  # error message, offset

    def __init__(self, sp_client, offset, limit=50, market="US"):
        super().__init__()
        self.sp_client = sp_client
        self.offset = offset
        self.limit = limit
        self.market = market

    def run(self):
        try:
            response = self.sp_client.current_user_saved_tracks(
                limit=self.limit, offset=self.offset, market=self.market
            )
            self.finished.emit(response["items"], self.offset)
        except Exception as e:
            self.error.emit(str(e), self.offset)


class PlaylistTrackFetchWorker(QThread):
    """Worker thread for fetching a batch of tracks at a specific offset"""

    finished = pyqtSignal(list, int)
    error = pyqtSignal(str, int)

    def __init__(self, sp_client, playlist_id, offset, limit=50, market="US"):
        super().__init__()
        self.sp_client = sp_client
        self.playlist_id = playlist_id
        self.offset = offset
        self.limit = limit
        self.market = market

    def run(self):
        try:
            response = self.sp_client.playlist_tracks(
                self.playlist_id,
                limit=self.limit,
                offset=self.offset,
                market=self.market,
            )
            self.finished.emit(response["items"], self.offset)
        except Exception as e:
            self.error.emit(str(e), self.offset)


class Spotify:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = [
            "user-library-read",
            "playlist-read-private",
            "playlist-read-collaborative",
        ]
        self.auth_manager = spotipy.oauth2.SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            scope=self.scope,
            redirect_uri="http://127.0.0.1:3000/callback",
            cache_path=".cache",
        )
        self.sp = spotipy.Spotify(auth_manager=self.auth_manager)
        self.market = "US"  # Default market, will be updated when user is fetched

    def get_client(self):
        return self.sp

    def get_user(self):
        user = self.sp.current_user()
        # Update market based on user's country
        if user and "country" in user:
            self.market = user["country"] or "US"
        return user

    def get_user_playlists(self, progress_callback=None):
        playlists = []
        response = self.sp.current_user_playlists()
        total = response.get("total", 0) or 0

        # include first page
        playlists.extend(response.get("items", []))
        if progress_callback and total > 0:
            progress_callback(min(99, int(len(playlists) / total * 100)))

        # paginate
        while response.get("next"):
            response = self.sp.next(response)
            playlists.extend(response.get("items", []))
            if progress_callback and total > 0:
                progress_callback(min(99, int(len(playlists) / total * 100)))

        if progress_callback:
            progress_callback(100)
        return playlists

    def get_playlist_tracks(self, playlist_id, max_workers=5, progress_callback=None):
        tracks = []
        response = self.sp.playlist_tracks(playlist_id)
        total = response["total"]

        batch_size = 50
        num_batches = math.ceil(total / batch_size)
        results = {}

        def fetch_batch(offset):
            try:
                response = self.sp.playlist_tracks(
                    playlist_id, limit=50, offset=offset, market=self.market
                )
                return offset, response["items"], None
            except Exception as e:
                return offset, [], str(e)

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(fetch_batch, batch_num * batch_size): batch_num
                for batch_num in range(num_batches)
            }

            completed = 0
            for future in as_completed(futures):
                offset, items, error = future.result()
                results[offset] = items
                completed += 1
                if progress_callback:
                    progress_callback(min(99, int(completed / num_batches * 100)))

        # Combine results in order
        tracks = []
        for batch_num in range(num_batches):
            offset = batch_num * batch_size
            if offset in results:
                tracks.extend(results[offset])

        if progress_callback:
            progress_callback(100)

        return tracks

    def get_user_tracks(self, max_workers=5, progress_callback=None):
        tracks = []
        response = self.sp.current_user_saved_tracks(
            limit=50, offset=0, market=self.market
        )
        total = response["total"]

        batch_size = 50
        num_batches = math.ceil(total / batch_size)
        results = {}

        def fetch_batch(offset):
            try:
                response = self.sp.current_user_saved_tracks(
                    limit=50, offset=offset, market=self.market
                )
                return offset, response["items"], None
            except Exception as e:
                return offset, [], str(e)

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(fetch_batch, batch_num * batch_size): batch_num
                for batch_num in range(num_batches)
            }

            completed = 0
            for future in as_completed(futures):
                offset, items, error = future.result()
                results[offset] = items
                completed += 1
                if progress_callback:
                    progress_callback(min(99, int(completed / num_batches * 100)))

        # Combine results in order
        tracks = []
        for batch_num in range(num_batches):
            offset = batch_num * batch_size
            if offset in results:
                tracks.extend(results[offset])

        if progress_callback:
            progress_callback(100)

        return tracks

    def get_playlist(self, playlist_id):
        return self.sp.playlist(playlist_id)
