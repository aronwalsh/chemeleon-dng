# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.4] - 2026-01-19

### Added
- Troubleshooting section in README for manual checkpoint download instructions
- Manual download instructions with wget command for Figshare
- Documentation for using custom checkpoint paths with `model_path` parameter
- pytest to dev dependencies in pyproject.toml
- tests directory for test suite

### Changed
- Updated Figshare download URL from `figshare.com/ndownloader` to `ndownloader.figshare.com` in `download_util.py`
- Updated tutorial notebook to reference version 0.1.4

### Fixed
- Improved checkpoint download reliability with corrected Figshare direct download URL
- Better handling of checkpoint download failures with manual fallback instructions

## [0.1.2] - 2025-10-28

### Added
- CLI entrypoint `chemeleon-dng` for improved command-line functionality

### Fixed
- Fixed PyPI distribution to include all subpackages (thanks to @ryannduma)

## [0.1.0] - 2025-10-08

### Added
- Initial release of Chemeleon-DNG framework
- Crystal Structure Prediction (CSP): predict stable structures from chemical formulas
- De Novo Generation (DNG): generate novel crystal structures
- Pretrained checkpoints for MP-20 and Alex-MP-20 datasets:
  - `chemeleon_csp_mp_20_v0.0.2.ckpt`
  - `chemeleon_dng_mp_20_v0.0.2.ckpt`
  - `chemeleon_csp_alex_mp_20_v0.0.2.ckpt`
  - `chemeleon_dng_alex_mp_20_v0.0.2.ckpt`
- Automatic checkpoint download from Figshare
- Tutorial notebook with usage examples
- PyPI distribution at https://pypi.org/project/chemeleon-dng/

[0.1.4]: https://github.com/hspark1212/chemeleon-dng/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/hspark1212/chemeleon-dng/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/hspark1212/chemeleon-dng/compare/v0.1.0...v0.1.2
[0.1.0]: https://github.com/hspark1212/chemeleon-dng/releases/tag/v0.1.0
