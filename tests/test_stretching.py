import json
import shutil
import subprocess
import sys

import pytest
from soundfile import read


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


class TestStretchingAccuracy:
    """Test time stretching accuracy with different ratios."""

    @pytest.mark.parametrize(
        "ratio, expected_duration",
        [
            (1.0, 5.0),  # No change
            (0.5, 10.0),  # Half speed = Double duration
            (2.0, 2.5),  # Double speed = Half duration
            (0.8, 6.25),  # 80% speed = 1.25x duration
            (1.25, 4.0),  # 125% speed = 0.8x duration
        ],
    )
    def test_stretch_ratio_duration(self, test_audio_file, temp_output_path, ratio, expected_duration):
        """Verify output duration matches the stretch ratio."""
        if not shutil.which("rubberband"):
            pytest.skip("rubberband-cli not installed")

        result = run_stretcher(test_audio_file, ratio, temp_output_path)
        assert result.returncode == 0

        data = json.loads(result.stdout)
        assert data["success"] is True

        y, sr = read(temp_output_path)
        duration = len(y) / sr

        # 5% tolerance
        assert abs(duration - expected_duration) < (expected_duration * 0.05), (
            f"Expected {expected_duration}s, got {duration}s"
        )


class TestErrorHandling:
    """Test error handling."""

    def test_missing_input_file(self, temp_output_path):
        result = run_stretcher("/nonexistent.wav", 1.0, temp_output_path)
        assert result.returncode != 0

    def test_invalid_ratio_zero(self, test_audio_file, temp_output_path):
        """Ratio must be positive."""
        result = run_stretcher(test_audio_file, 0.0, temp_output_path)
        # Should fail (rubberband can't process 0 duration)
        assert result.returncode != 0

    def test_invalid_ratio_negative(self, test_audio_file, temp_output_path):
        result = run_stretcher(test_audio_file, -1.0, temp_output_path)
        assert result.returncode != 0
