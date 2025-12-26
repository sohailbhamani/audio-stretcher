# audio-stretcher

Time-stretch CLI for tempo normalization and pitch shifting. Wraps [Rubberband](https://breakfastquay.com/rubberband/).

## Features

- **Tempo Normalization** — Match tracks to target BPM
- **Pitch Shifting** — Change key without affecting tempo
- **Time Stretching** — Change tempo without affecting pitch
- **High Quality** — Minimal artifacts

## Installation

```bash
pip install audio-stretcher
```

## Usage

```bash
# Stretch to target BPM
audio-stretcher stretch track.mp3 --bpm 128

# Pitch shift by semitones
audio-stretcher pitch track.mp3 --semitones 2

# Combine tempo and pitch
audio-stretcher stretch track.mp3 --bpm 130 --semitones -1
```

## Requirements

- Python 3.9+
- Rubberband

## License

GPL-3.0 — See [LICENSE](LICENSE)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
