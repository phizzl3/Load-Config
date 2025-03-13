"""
* This is a sample configuration module for loading JSON data *

This module loads configuration data from a JSON file,
applies default values if the file is not found,
and processes the data to generate a configuration dictionary for import.

Modify this module to use loadconfig.py to suit your needs in loading your
configuration data.
"""

from pathlib import Path

# TODO Import the load_config function from its relative path
from .loadconfig import load_config

# TODO Update to your desired JSON file location
JSON = Path().home() / "PyAppFiles" / "My Application" / "config.json"

# TODO Update to your Default values for your JSON data
DEFAULTS = {
    "random number": 20,
    "working folder name": "Combine_PDFs",
    "output file name": "_Merged_PDF.pdf",
}

# Load (or set defaults) config json data
data = load_config(json_path=JSON, default_data=DEFAULTS)

# TODO Work with the JSON data to generate your configuration values
important_number = data["random number"] ** 2
working_dir = data["working folder name"][3:]
file_name = data["output file name"].lower()

# TODO Update this formatted config data (Import this)
CONFIG = {
    "number": important_number,
    "merge folder": Path().home() / working_dir,
    "output file": file_name,
}

# TODO Or just load the config JSON data without modification (OR Import this)
CONFIG2 = load_config(json_path=JSON, default_data=DEFAULTS)
