import json
import logging
import sys
from pathlib import Path

import click
import pyrubberband as pyrb
import soundfile as sf

# Configure logging to stderr
logging.basicConfig(level=logging.INFO, stream=sys.stderr, format="%(message)s")
logger = logging.getLogger("audio-stretcher")


@click.group()
def cli():
    """Audio Stretcher CLI using Rubberband (high quality)."""
    pass


@cli.command()
@click.argument("input_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--ratio",
    type=float,
    required=True,
    help="Time stretch ratio (e.g. 1.0 = same, 2.0 = double speed/half duration)",
)
@click.option(
    "--output",
    "output_path",
    type=click.Path(path_type=Path),
    required=True,
    help="Output file path",
)
def stretch(input_path: Path, ratio: float, output_path: Path):
    """Time-stretch audio file and save to output."""
    try:
        # Load audio using soundfile (pyrubberband works with numpy arrays)
        y, sr = sf.read(str(input_path))

        # Perform time stretch
        # pyrubberband.time_stretch(y, sr, rate) where rate > 1.0 is faster
        y_stretched = pyrb.time_stretch(y, sr, ratio)

        # Save output
        sf.write(str(output_path), y_stretched, sr)

        result = {"success": True, "output_path": str(output_path), "ratio": ratio}
        click.echo(json.dumps(result))

    except Exception as e:
        logger.error(f"Stretching failed: {e}")
        # Check if rubberband binary is missing
        if "rubberband" in str(e).lower() and "file not found" in str(e).lower():
            logger.error("NOTE: 'rubberband-cli' system package is required.")
        sys.exit(1)


if __name__ == "__main__":
    cli()
