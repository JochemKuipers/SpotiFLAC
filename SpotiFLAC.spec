# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['SpotiFLAC.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('Assets', 'Assets'),
        ('Services', 'Services'),
        ('Utils', 'Utils'),
    ],
    hiddenimports=[
        'qdarktheme',
        'packaging',
        'requests',
        'PyQt6.QtCore',
        'PyQt6.QtGui',
        'PyQt6.QtWidgets',
        'PyQt6.QtNetwork'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SpotiFLAC',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    coerce_archive_to_exe=False,
    icon='Assets/icon.ico'
)
