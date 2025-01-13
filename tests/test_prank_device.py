# tests/test_prank_device.py

import pytest
from pathlib import Path
import sys
from src.prank_device import PrankDevice

@pytest.fixture
def device():
    """Create a PrankDevice instance for testing"""
    dev = PrankDevice()
    yield dev
    dev.cleanup()

def test_init(device):
    """Test device initialization"""
    assert device.ldr_pin == 4
    assert isinstance(device.sound_dir, Path)

def test_is_dark(device):
    """Test darkness detection"""
    # Test multiple times since we're using random values in mock
    results = [device.is_dark(threshold=500) for _ in range(100)]
    # Should get both True and False results with mock values
    assert True in results
    assert False in results

def test_list_sound_files(device, tmp_path):
    """Test sound file listing"""
    # Create temporary sound files
    sound_dir = tmp_path / "sounds"
    sound_dir.mkdir()
    (sound_dir / "test1.mp3").touch()
    (sound_dir / "test2.mp3").touch()
    (sound_dir / "not_sound.txt").touch()
    
    device.sound_dir = sound_dir
    sound_files = device.list_sound_files()
    
    assert len(sound_files) == 2
    assert all(f.suffix == '.mp3' for f in sound_files)

def test_cleanup(device):
    """Test cleanup method"""
    device.cleanup()  # Should not raise any errors