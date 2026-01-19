"""Minimal tests for download_util module."""

import tempfile
from pathlib import Path

from chemeleon_dng.download_util import (
    FIGSHARE_URL,
    download_file,
    ensure_checkpoints_downloaded,
)


def test_figshare_url_format():
    """Test that FIGSHARE_URL uses ndownloader.figshare.com domain."""
    assert FIGSHARE_URL == "https://ndownloader.figshare.com/files/54966305"
    assert FIGSHARE_URL.startswith("https://ndownloader.figshare.com")


def test_actual_download():
    """Test actual download from Figshare."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test_download.tar.gz"

        # Download the file
        download_file(FIGSHARE_URL, test_file)

        # Verify file was downloaded and has content
        assert test_file.exists()
        assert test_file.stat().st_size > 100_000_000  # at least 100MB


def test_ensure_checkpoints_downloaded():
    """Test that checkpoints are downloaded and extracted to temp directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        ckpt_dir = Path(tmpdir) / "ckpts"

        # Download and extract checkpoints
        ensure_checkpoints_downloaded(str(ckpt_dir))

        # Verify directory exists
        assert ckpt_dir.exists()
        assert ckpt_dir.is_dir()

        # Verify checkpoint files exist
        ckpt_files = list(ckpt_dir.glob("*.ckpt"))
        assert len(ckpt_files) > 0, "No checkpoint files found"
