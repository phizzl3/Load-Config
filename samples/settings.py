"""

Load (use defaults first if not found) json data from
file, and use that data to generate a settings file for import.

"""

from pathlib import Path
from loadjsondata import loadjson


# json file location
JSON = Path().home() / "PyAppFiles" / "Combine PDFs" / "settings.json"

# Default values for json data
DEFAULTS = {
    "random number": 20,
    "working folder name": "Combine_PDFs",
    "output file name": "_Merged_PDF.pdf",
}

# Load (or set defaults) settings json data
data = loadjson(JSON, default_data=DEFAULTS)

# Do stuff with data
important_number = data["random number"] ** 2
working_dir = data["working folder name"][3:]
file_name = data["output file name"].lower()

# Formatted settings data (Import this)
SETTINGS = {
    "number": important_number,
    "merge folder": Path().home() / working_dir,
    "output file": file_name
}

# Or just load the json data (Import this)
SETTINGS_2 = loadjson(JSON, default_data=DEFAULTS)
