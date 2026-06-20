# generate_tracks.py

import json
from pathlib import Path

MEDIA_DIR = Path("media")
OUTPUT_FILE = Path("tracks.json")

AUDIO_EXTENSIONS = {
    ".mp3",
    ".m4a",
    ".aac",
    ".ogg",
    ".wav",
    ".flac"
}

tracks = sorted(
    [
        f"media/{file.name}"
        for file in MEDIA_DIR.iterdir()
        if file.is_file() and file.suffix.lower() in AUDIO_EXTENSIONS
    ],
    key=lambda x: x.lower()
)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(tracks, f, ensure_ascii=False, indent=2)

print(f"✓ {len(tracks)} Tracks nach {OUTPUT_FILE} geschrieben")