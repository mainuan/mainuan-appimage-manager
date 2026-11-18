#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mainuan AppImage Manager 1.0.3 - AppImage Integration Manager
Main application entry point.
"""

import sys
import os
import signal
import gettext
import locale
from pathlib import Path

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gdk, Gio

PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))
LOCALE_DIR = PROJECT_ROOT / 'locale'
ASSETS_DIR = PROJECT_ROOT / 'assets'

GLib.set_prgname('org.mainuan.appimagemanager')
GLib.set_application_name('Mainuan AppImage Manager')
Gtk.Window.set_default_icon_name('org.mainuan.appimagemanager')
if hasattr(Gdk, 'set_program_class'):
    Gdk.set_program_class('org.mainuan.appimagemanager')



def _system_languages():
    """System language preference list, most specific first (e.g. pt_BR, pt)."""
    names = []
    for raw in GLib.get_language_names():
        name = raw.split('.')[0].split('@')[0].replace('-', '_')
        if name and name not in ('C', 'POSIX') and name not in names:
            names.append(name)
    return names


def _setup_translation():
    """The UI language always follows the system language (no manual choice)."""
    try:
        locale.setlocale(locale.LC_ALL, '')
    except locale.Error:
        pass
    gettext.bindtextdomain('mainuan-appimage-manager', str(LOCALE_DIR))
    gettext.textdomain('mainuan-appimage-manager')
    translation = gettext.translation(
        'mainuan-appimage-manager', str(LOCALE_DIR),
        languages=_system_languages() or None, fallback=True)
    return translation.gettext


_ = _setup_translation()

from core.appimage_manager import AppImageManager
from ui.main_window import MainWindow
from utils.environment import get_environment_detector
from ui import theme as mn_theme


class MainuanAppImageManagerApplication(Gtk.Application):
    """Main application class."""

    def __init__(self):
        super().__init__(
            application_id='org.mainuan.appimagemanager',
            flags=Gio.ApplicationFlags.FLAGS_NONE
        )
        self.app_path = PROJECT_ROOT
        self.assets_path = ASSETS_DIR
        self.window = None

        self.connect('startup', self.on_startup)
        self.connect('activate', self.on_activate)
        self.connect('shutdown', self.on_shutdown)

        self.environment_detector = get_environment_detector()

        signal.signal(signal.SIGINT, self._handle_signal)
        signal.signal(signal.SIGTERM, self._handle_signal)

    def _handle_signal(self, signum, frame):
        self.quit()

    def on_startup(self, app):
        # Mainuan Store look; follows the system light/dark mode automatically
        mn_theme.start()
        self.appimage_manager = AppImageManager()

        about_action = Gio.SimpleAction.new('about', None)
        about_action.connect('activate', lambda *_: self.window._show_about() if self.window else None)
        self.add_action(about_action)

    def on_activate(self, app):
        if self.window:
            self.window.present()
            return

        self.window = MainWindow(
            self, self.appimage_manager,
            self.environment_detector, _, self.assets_path
        )
        self.window.show_all()

    def on_shutdown(self, app):
        self._cleanup_garbage()

    def _cleanup_garbage(self):
        import shutil
        from config.constants import TMP_DIR
        try:
            if TMP_DIR.exists():
                shutil.rmtree(str(TMP_DIR), ignore_errors=True)
        except Exception:
            pass
        try:
            for root, dirs, _ in os.walk(self.app_path):
                if '__pycache__' in dirs:
                    shutil.rmtree(os.path.join(root, '__pycache__'), ignore_errors=True)
        except Exception:
            pass


def main():
    app = MainuanAppImageManagerApplication()
    return app.run(sys.argv)


if __name__ == '__main__':
    sys.exit(main())
