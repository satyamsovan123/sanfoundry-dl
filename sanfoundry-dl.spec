# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['run.py'],
    pathex=[],
    binaries=[],
    datas=[("app/constants", "app/constants"), ("app/gui", "app/gui"), ("app/main", "app/main"), ("app/services", "app/services"), ('assets', 'assets')],
    hiddenimports=[
        'altgraph', 'attrs', 'blinker', 'certifi', 'chardet', 'click', 
        'flask', 'flask_cors', 'h11', 'idna', 'itsdangerous', 'jinja2', 'macholib', 'markupsafe', 
        'outcome', 'packaging', 'pillow', 'pyinstaller', 'pyinstaller_hooks_contrib', 'pysocks', 
        'python_dotenv', 'reportlab', 'requests', 'selenium', 'setuptools', 'sniffio', 
        'sortedcontainers', 'tk', 'trio', 'trio_websocket', 'typing_extensions', 'urllib3', 
        'webdriver_manager', 'websocket', 'werkzeug', 'wsproto'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='sanfoundry-dl',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
