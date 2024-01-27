"""

Checks to see if a json file exists at json_path, and returns a 
python data type of the contents read from the json file. If the 
json file doesn't exist, outputs json file using the python data 
type (json compatible) optionally passed as default_data, then 
loads from the file.

Args:
    json_path (Path): pathlib.Path pointing to json file location.
    
    default_data (any, optional): python data type (json compatible) 
    to output to json file. Defaults to None.

Returns:
    any: python data type read from json data.
    
"""

__version__ = "1.0.1"

import json
from pathlib import Path


def loadjson(json_path: Path, default_data=None):
    """Checks to see if a json file exists at json_path, and returns a
    python data type of the contents read from the json file. If the
    json file doesn't exist, outputs json file using the python data
    type (json compatible) optionally passed as default_data, then 
    loads from the file.

    Args:
        json_path (Path): pathlib.Path pointing to json file location.
        default_data (any, optional): python data type (json compatible) to 
        output to json file. Defaults to None.

    Returns:
        any: python data type read from json data.
    """
    # Convert to Path if passed as str
    if not isinstance(json_path, Path):
        json_path = Path(json_path)
    # Checks to see if the target file exists and creats
    # the folder path if it doesn't exist.
    if not json_path.exists():
        if not json_path.parent.is_dir():
            json_path.parent.mkdir(parents=True)

        if default_data:
            # Writes the python data to output json file.
            with open(json_path, "w", encoding="utf-8") as json_file:
                json.dump(default_data, json_file, indent=4)
        else:
            input(f"\n File not found:\n {json_path}")

    # Load the data from the json file at the target location.
    with open(json_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)
