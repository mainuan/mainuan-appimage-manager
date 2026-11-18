from setuptools import setup, find_packages

setup(
    name='mainuan-appimage-manager',
    version='1.0.3',
    description='AppImage integration manager for Mainuan Linux',
    author='David Caixinha',
    author_email='tugatechlab.contacto@gmail.com',
    license='GPL-3.0+',
    packages=find_packages(),
    python_requires='>=3.10',
    data_files=[
        ('share/applications', ['debian/org.mainuan.appimagemanager.desktop']),
        ('share/metainfo', ['debian/org.mainuan.appimagemanager.metainfo.xml']),
        ('share/man/man1', ['docs/mainuan-appimage-manager.1']),
        ('share/icons/hicolor/48x48/apps', ['assets/icons/48x48/org.mainuan.appimagemanager.png']),
        ('share/icons/hicolor/64x64/apps', ['assets/icons/64x64/org.mainuan.appimagemanager.png']),
        ('share/icons/hicolor/128x128/apps', ['assets/icons/128x128/org.mainuan.appimagemanager.png']),
        ('share/mainuan-appimage-manager/assets/themes', [
            'assets/themes/base.css',
            'assets/themes/dark.css',
            'assets/themes/light.css',
        ]),
        ('share/locale/de/LC_MESSAGES', ['locale/de/LC_MESSAGES/mainuan-appimage-manager.mo']),
        ('share/locale/en/LC_MESSAGES', ['locale/en/LC_MESSAGES/mainuan-appimage-manager.mo']),
        ('share/locale/es/LC_MESSAGES', ['locale/es/LC_MESSAGES/mainuan-appimage-manager.mo']),
        ('share/locale/fr/LC_MESSAGES', ['locale/fr/LC_MESSAGES/mainuan-appimage-manager.mo']),
        ('share/locale/it/LC_MESSAGES', ['locale/it/LC_MESSAGES/mainuan-appimage-manager.mo']),
        ('share/locale/pt/LC_MESSAGES', ['locale/pt/LC_MESSAGES/mainuan-appimage-manager.mo']),
        ('share/locale/pt_BR/LC_MESSAGES', ['locale/pt_BR/LC_MESSAGES/mainuan-appimage-manager.mo']),
        ('share/locale/ro/LC_MESSAGES', ['locale/ro/LC_MESSAGES/mainuan-appimage-manager.mo']),
        ('share/locale/ru/LC_MESSAGES', ['locale/ru/LC_MESSAGES/mainuan-appimage-manager.mo']),
    ],
    entry_points={
        'console_scripts': [
            'mainuan-appimage-manager=main:main',
        ],
    },
)
