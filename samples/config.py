"""
Load (use defaults first if not found) config json data from
file, and use that data to generate a config.py file for import.
"""

from pathlib import Path

from .loadconfig import load_config

# json file location
JSON = Path().home() / "PyAppFiles" / "My Application" / "config.json"

# Default values for json data
DEFAULTS = {
    "random number": 20,
    "working folder name": "Combine_PDFs",
    "output file name": "_Merged_PDF.pdf",
}

# Load (or set defaults) config json data
data = load_config(json_path=JSON, default_data=DEFAULTS)

# Do stuff with data
important_number = data["random number"] ** 2
working_dir = data["working folder name"][3:]
file_name = data["output file name"].lower()

# Formatted config data (Import this)
CONFIG = {
    "number": important_number,
    "merge folder": Path().home() / working_dir,
    "output file": file_name,
}

# Or just load the config json data (Import this)
CONFIG = load_config(json_path=JSON, default_data=DEFAULTS)
