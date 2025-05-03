# config.py
from pathlib import Path

# Base directory (the directory where config.py is located)
BASE_DIR = Path(__file__).parent.parent


# Define constants
SONG_DATABASE_PATH = BASE_DIR / "database.xlsx"
SORTED_SONG_DATABASE_PATH = BASE_DIR / "database_sorted.xlsx"