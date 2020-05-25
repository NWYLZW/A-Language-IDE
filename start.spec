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
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='AL-IDE_1.1.0.0',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=['./upx-3.96'],
          runtime_tmpdir=None,
          console=False, icon='AL-IDE.ico')
