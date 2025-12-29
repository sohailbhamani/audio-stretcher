# Audio Stretcher

[![CI](https://github.com/sohailbhamani/audio-stretcher/actions/workflows/ci.yml/badge.svg)](https://github.com/sohailbhamani/audio-stretcher/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

A GPL-licensed CLI tool for high-quality audio time-stretching using Rubberband. Perfect for tempo adjustment without pitch change.

## Features

- **High-Quality Time Stretching**: Uses Rubberband library for professional-grade results
- **Preserve Pitch**: Time stretch without affecting pitch (phase vocoder with transient preservation)
- **JSON Output**: Returns success status and output file path

## Prerequisites

This tool requires the `rubberband` binary:

```bash
# Ubuntu/Debian
sudo apt-get install rubberband-cli

# macOS
brew install rubberband
```

## Installation

```bash
# Clone the repository
git clone https://github.com/sohailbhamani/audio-stretcher.git
cd audio-stretcher

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install in development mode
pip install -e ".[dev]"
```

## Usage

```bash
# Time-stretch an audio file (ratio > 1 = faster, < 1 = slower)
audio-stretcher stretch input.wav --ratio 1.5 --output output.wav
```

### Output

```json
{
  "success": true,
  "output_path": "output.wav",
  "ratio": 1.5
}
```

## Development

```bash
# Run tests
pytest

# Run linter
ruff check .

# Run type checker
mypy src/
```

## Dependencies

- [pyrubberband](https://github.com/bmcfee/pyrubberband) - Python wrapper for Rubberband
- [Rubberband](https://breakfastquay.com/rubberband/) - High-quality audio time-stretching library
- [soundfile](https://python-soundfile.readthedocs.io/) - Audio file I/O
- [Click](https://click.palletsprojects.com/) - CLI framework

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
