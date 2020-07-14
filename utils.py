from pathlib import Path
import os
import json

ABS_PATH = Path(__file__).parent.absolute()
CACHE_DIR = os.path.join(os.environ["HOME"], ".cache", "wal")


def get_glade_file_path(name):
    return os.path.join(ABS_PATH, 'ui', name)


def get_json_file():
    return os.path.join(ABS_PATH, 'events.json')


def get_wal_colors():
    file_name = os.path.join(CACHE_DIR, "colors.json")
    if not os.path.exists(file_name):
        # load a default if not exists
        file_name = os.path.join(ABS_PATH, 'colors.json')
    with open(file_name) as file:
        j = json.load(file)
        return j["colors"]
