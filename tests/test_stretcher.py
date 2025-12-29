import json
import os
import shutil
import subprocess
import sys
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
    """Create a temporary sine wave audio file (5.0 seconds)."""
    audio = generate_tone(440, 5.0)

    fd, path = tempfile.mkstemp(suffix=".wav")
    os.close(fd)
    sf.write(path, audio, SAMPLE_RATE)

    yield path

    if os.path.exists(path):
        os.remove(path)


def run_stretcher(file_path, ratio, output_path):
    cmd = [
        sys.executable,
        "-m",
        "audio_stretcher.main",
        "stretch",
        str(file_path),
        "--ratio",
        str(ratio),
        "--output",
        str(output_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result


def test_stretch_ratio(test_audio_file):
    """Verify time stretching ratio affects duration."""
    if not shutil.which("rubberband"):
        pytest.fail("rubberband not found, cannot test stretching")

    fd, output_path = tempfile.mkstemp(suffix="_out.wav")
    os.close(fd)

    try:
        # Ratio 2.0 = Double speed = Half duration (2.5s)
        result = run_stretcher(test_audio_file, 2.0, output_path)
        assert result.returncode == 0

        data = json.loads(result.stdout)
        assert data["success"] is True

        # Check output duration
        y, sr = sf.read(output_path)
        duration = len(y) / sr

        # Expect approx 2.5s
        assert abs(duration - 2.5) < 0.1, f"Expected 2.5s duration, got {duration}s"

    finally:
        if os.path.exists(output_path):
            os.remove(output_path)
