# SpotiFLAC Enhanced 🎵

> **⚠️ This is a fork of the original [SpotiFLAC](https://github.com/afkarxyz/SpotiFLAC) project with additional features and improvements**

[![GitHub All Releases](https://img.shields.io/github/downloads/JochemKuipers/SpotiFLAC/total?style=for-the-badge)](https://github.com/JochemKuipers/SpotiFLAC/releases)

![SpotiFLAC](https://github.com/user-attachments/assets/b4c4f403-edbd-4a71-b74b-c7d433d47d06)

**SpotiFLAC Enhanced** allows you to download Spotify tracks in true FLAC format through services like Tidal and Deezer, with the added feature of Spotify account integration.

## 🚀 What's New in This Fork

### ✨ New Features
- **Spotify Account Integration**: Connect your Spotify account to fetch playlists and liked songs directly

## 📥 Download

### Latest Release
[![Download Latest](https://img.shields.io/badge/Download-Latest%20Release-blue?style=for-the-badge)](https://github.com/JochemKuipers/SpotiFLAC/releases/latest)

### Original Project
For the original SpotiFLAC project, visit: [afkarxyz/SpotiFLAC](https://github.com/afkarxyz/SpotiFLAC)

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/180b8322-ce2d-4842-a5dd-ac4d7b7a5efa)

![image](https://github.com/user-attachments/assets/3f84d53b-2da1-4488-986c-772b82832f2d)

![image](https://github.com/user-attachments/assets/f604dc04-4ee6-4084-b314-0be7cd5d7ef9)

![image](https://github.com/user-attachments/assets/40264f32-f2cf-4e91-b09d-fb628d9771f7)

## 🎧 Lossless Audio Check

![image](https://github.com/user-attachments/assets/d63b422d-0ea3-4307-850f-96c99d7eaa9a)

![image](https://github.com/user-attachments/assets/7649e6e1-d5d1-49b3-b83f-965d44651d05)

### [Download](https://github.com/afkarxyz/SpotiFLAC/releases/download/v0/FLAC-Checker.zip) FLAC Checker

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Spotify Developer Account (for account integration features)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/JochemKuipers/SpotiFLAC.git
   cd SpotiFLAC
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python SpotiFLAC.py
   ```

### Spotify Account Setup (Optional)
To use the Spotify account integration features:
1. Create a Spotify Developer App at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Set the redirect URI to `http://localhost:8080/callback`
3. Add your Client ID and Client Secret in the application settings

## 📋 Features

### Core Features
- **FLAC Quality Downloads**: Download tracks in true FLAC format
- **Multiple Sources**: Support for Tidal and Deezer
- **ISRC Matching**: Automatic track matching using ISRC codes
- **Metadata Preservation**: Complete metadata and album art preservation

### Enhanced Features (This Fork)
- **Spotify Integration**: Direct playlist and liked songs fetching

## 🔧 Configuration

### Tidal API Configuration
The application supports multiple Tidal API endpoints with automatic fallback:
- Default: `https://hifi.401658.xyz`
- Auto mode: Automatically selects the best available endpoint

### Service Selection
Choose between:
- **Tidal**: High-quality FLAC downloads with extensive metadata
- **Deezer**: Alternative source with good track availability

## 🤝 Contributing

This is a fork of the original SpotiFLAC project. If you'd like to contribute:

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project maintains the same license as the original SpotiFLAC project.

## 🙏 Acknowledgments

- **Original Project**: [afkarxyz/SpotiFLAC](https://github.com/afkarxyz/SpotiFLAC) - The original SpotiFLAC project
- **Contributors**: All contributors to both the original project and this fork
- **Services**: Tidal and Deezer for providing high-quality audio sources

## 📞 Support

- **Issues**: [Report issues](https://github.com/JochemKuipers/SpotiFLAC/issues) for this fork
- **Original Project**: [Original project issues](https://github.com/afkarxyz/SpotiFLAC/issues)

---

**Note**: This is an enhanced fork of the original SpotiFLAC project. For the original project, please visit [afkarxyz/SpotiFLAC](https://github.com/afkarxyz/SpotiFLAC).
