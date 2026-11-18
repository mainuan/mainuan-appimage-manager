# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/lang/en/).

### 🎉 Initial Release --> [1.0.3] - 2026-11-17

## Types of Changes

- **Added** for new features
- **Changed** for changes in existing functionality
- **Deprecated** for features soon to be removed
- **Removed** for now removed features
- **Fixed** for any bug fixes
- **Security** in case of vulnerabilities

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

## Contribute

To report bugs or request features:
- **Issues**: https://github.com/MainuanLinux/mainuan-grub-editor/issues
- **Discussions**: https://github.com/MainuanLinux/mainuan-grub-editor/discussions
- **Email**: info@mainuanlinux.com

To contribute translations:
1. Create file `translations/locales/XX.py` (XX = language code)
2. Copy structure from `translations/locales/en.py`
3. Translate all `STRINGS`
4. Add language to `SUPPORTED_LANGUAGES` in `strings.py`
5. Submit Pull Request


## Support

- **Documentation**: https://mainuan.org/docs/mainuan-grub-editor
- **Community**: https://mainuan.org/community
- **Support**: support@mainuanlinux.com
