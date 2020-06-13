# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# 外置文件
addedFiles = [
    ('./visualizationSrc/Data/','./visualizationSrc/Data/'),
    ('C:\\Users\\Superme\\AppData\\Roaming\\Python\\Python37\\site-packages\\Python.Runtime.dll','.'),
]

a = Analysis(['start.py'],
             pathex=['./'],
             binaries=[],
             datas=addedFiles,
             hiddenimports=['clr'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AL-IDE',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=['./upx-3.96'],
    console=False, icon='AL-IDE.ico')
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=['./upx-3.96'],
    name='ALIDE【原石计划Mod开发IDE】')
