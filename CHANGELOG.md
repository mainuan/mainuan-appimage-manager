# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/lang/en/).

## [1.0.3] - 2026-11-14

### 🐛 Fixed
- Button icons and the minimize / maximize / close buttons were almost invisible (light theme) or missing (dark theme). Icons are now drawn by the app itself with the theme colours, independent of the system icon theme; the window buttons are the app's own and sit on the right.

## [1.0.2] - 2026-11-14

### 🎨 Changed
- New round application icon (Mainuan teal with an AppImage package), installed in every hicolor size.
- Interface restyled to match Mainuan Store: same colour palette, rounded cards, buttons and fields. Functions and menus are unchanged.
- Light and dark themes follow the system automatically (also while the app is open); labels and status colours adapt to both.
- Window title bar now has the logo and the MINIMIZE, MAXIMIZE and CLOSE buttons on the right.
- Language always follows the system language (pt_BR, pt, en, es, fr, de, it, ro, ru); there is no language selector in the app.

## [Unreleased]

### ✨ Added
- **Brazilian Portuguese (pt_BR)**: new `pt_BR` translation using Brazilian vocabulary (e.g. "Arquivo", "Salvar", "Excluir", "Verificando atualizações…"), plus `pt_BR` entries in the `.desktop` file and AppStream metadata. The existing `pt` translation remains European Portuguese.

### 🎨 Changed
- Rebranded from Soplos AppImage Manager to Mainuan AppImage Manager: package, command, application ID (`org.mainuan.appimagemanager`), translation domain, theme variables, documentation and contact details. The maintainer is now David Caixinha; the original copyright notice of Sergi Perich is kept alongside it.
- Accent colour changed from orange (`#ff8800`) to the blue-turquoise of the Mainuan logo (`#08c8d0`, hover `#2ad8e0`). The theme variable `soplos_orange` is now `mainuan_blue`.
- Application icon and `assets/icons/logo.png` recoloured from orange to the same blue. Every hicolor size is now generated from the master image instead of shipping the full-size image in each folder.

---

## [1.0.1-2] - 2026-07-20

### ✨ Added
- **Copy instead of move**: When adding an AppImage (via the "+" button or by dragging and dropping it onto the window), you can now choose to keep the original file and copy it into `~/AppImages/` instead of moving it — useful when the AppImage lives in a folder synced across multiple machines

---

## [1.0.1-1] - 2026-07-07

### 🔧 Changed
- Build dependency `python3-all` replaced with `python3`.

---

## [1.0.1] - 2026-03-30

### ✨ Added
- **Properties dialog**: View and edit name, version, description, categories and update URL for each integrated AppImage
- **Automatic update checking**: Checks for updates via GitHub, GitLab and Codeberg release APIs, direct URL comparison (`Last-Modified` header), or embedded `appimageupdatetool` info
- **Check All Updates**: New button in the header bar checks all AppImages with a configured update source at once — replaces the Refresh button
- **Update All**: From the Check All Updates dialog, update every AppImage that has a newer version available in one action
- **Run as root**: Toggle in Properties to launch any AppImage with `pkexec` — a PolicyKit authentication dialog appears on launch; the preference is stored in the `.desktop` file as `X-AppImage-RunAsRoot=true`

### 🔧 Fixed
- **Icon extraction**: Improved icon search — handles relative symlinks, case-insensitive matching, pixmaps directories and additional hicolor sizes
- **Hardcoded UI strings**: All visible UI text now passes through the translation system; several strings were previously displayed in English regardless of locale
- **Translation coverage**: All 8 languages (de, en, es, fr, it, pt, ro, ru) now have full coverage including all new strings added in this release
- **Theme Support**: Fixed dark mode being forced on light themes; the application now correctly respects the system's light or dark GTK theme preference

---

## [1.0.0-1] - 2026-03-22

### 🔧 Fixed
- **UI colors**: Fixed background color inconsistency — window, list and scrolled area now consistently use the correct Mainuan dark theme color (#2b2b2b).

---

## [1.0.0] - 2026-03-22

### 🎉 Initial Release

#### Core
- Add AppImages via file chooser — file moved to `~/AppImages/` automatically
- Drag and drop AppImage files directly onto the window
- Automatic metadata extraction: icon, name, version and description from the AppImage itself
- Icons saved persistently to `~/AppImages/.icons/`
- Desktop entry creation in `~/.local/share/applications/`
- Supports AppImage Type 1 (ISO9660) and Type 2 (SquashFS)
- Extraction engine: `7zz` preferred, `--appimage-extract` fallback

#### Integration
- Universal detection: recognises AppImages from any source (Mainuan Welcome, manual placement, third-party tools)
- One-click Integrate button for AppImages already present in `~/AppImages/`
- Auto-refresh via dual file monitor — watches `~/AppImages/` and `~/.local/share/applications/` with 500 ms debounce

#### Management
- Run AppImages directly from the manager
- Delete AppImage, icon and `.desktop` entry in one action
- Update URL detection via `readelf` parsing of the `.upd_info` ELF section
- Supports `zsync`, `gh-releases-zsync` and direct HTTP/HTTPS update formats

#### Interface
- About dialog (F1 shortcut + GNOME app menu entry)
- Status bar showing desktop environment and display protocol
- Internationalisation: 8 languages (es, en, fr, de, it, pt, ro, ru)
- Mainuan Linux ecosystem UI style

---

## Author

Developed and maintained by David Caixinha
Contact: tugatechlab.contacto@gmail.com

## Contributing

- **Email**: tugatechlab.contacto@gmail.com

## Support

- **Documentation**:
