"""Shared test fixtures for audio-stretcher tests."""

import os
import tempfile

import numpy as np
import pytest
import soundfile as sf

SAMPLE_RATE = 44100


def generate_tone(freq, duration, amp=0.5):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    return amp * np.sin(2 * np.pi * freq * t)


@pytest.fixture
def test_audio_file():
    """Create a temporary sine wave audio file (5.0 seconds).

    Returns:
        str: Path to the temporary wav file.
    """
    audio = generate_tone(440, 5.0)

    fd, path = tempfile.mkstemp(suffix=".wav")
    os.close(fd)
    sf.write(path, audio, SAMPLE_RATE)

    yield path

    if os.path.exists(path):
        os.remove(path)


@pytest.fixture
def temp_output_path():
    """Create a temporary path for output file."""
    fd, path = tempfile.mkstemp(suffix="_out.wav")
    os.close(fd)

    yield path

    if os.path.exists(path):
        os.remove(path)
