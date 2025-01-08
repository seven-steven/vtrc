# -*- mode: python ; coding: utf-8 -*-
import os
import platform
import PyQt6
from PyInstaller.utils.hooks import collect_all

block_cipher = None

# 获取 PyQt6 的安装路径
pyqt_path = os.path.dirname(PyQt6.__file__)
qt_bin_path = os.path.join(pyqt_path, "Qt6", "bin")

# 收集 PyQt6 相关的所有文件
qt_data = []
binaries = []
hiddenimports = []

# 添加基本的 PyQt6 模块
packages = [
    'PyQt6',
    'PyQt6.QtCore',
    'PyQt6.QtGui',
    'PyQt6.QtWidgets',
    'PyQt6.sip',
]

for package in packages:
    col_data, col_binaries, col_hidden = collect_all(package)
    qt_data.extend(col_data)
    binaries.extend(col_binaries)
    hiddenimports.extend(col_hidden)

# 添加 Qt6 核心 DLL 文件
if platform.system() == 'Windows':
    required_dlls = [
        'Qt6Core.dll',
        'Qt6Gui.dll',
        'Qt6Widgets.dll',
        'Qt6Svg.dll',
        'Qt6Network.dll',
    ]
    for dll in required_dlls:
        dll_path = os.path.join(qt_bin_path, dll)
        if os.path.exists(dll_path):
            binaries.append((dll_path, '.'))

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries,
    datas=qt_data,
    hiddenimports=hiddenimports + [
        'pkgutil',
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
    name='VTRC.exe' if platform.system() == 'Windows' else 'VTRC',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # 临时设置为 True 以查看错误信息
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if platform.system() == 'Windows' else ('icon.icns' if platform.system() == 'Darwin' else 'icon.png'),
)

# macOS 打包配置
if platform.system() == 'Darwin':
    app = BUNDLE(
        exe,
        name='VTRC.app',
        icon='icon.icns',
        bundle_identifier=None,
    )