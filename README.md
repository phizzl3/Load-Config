# Load-Config

Load-Config is a Python utility that checks for the existence of a JSON configuration file at a specified path and returns the contents as a Python data type. If the JSON file does not exist, it creates the file using optionally provided default data and then loads the data from the file.

## Features

- Load configuration data from a JSON file.
- Automatically create a JSON file with default data if it does not exist.
- Simple and easy-to-use interface.

## Installation

To install Load-Config, simply clone the repository and install the required dependencies:

```sh
git clone https://github.com/yourusername/load-config.git
cd load-config
pip install -r requirements.txt
```

## Usage

```py
import loadconfig
from pathlib import Path

# Define the path to the JSON configuration file
json_path = Path("/Volumes/USB/config.json")

# Optionally, define default data to be written if the file does not exist
default_data = {
    "setting1": "value1",
    "setting2": "value2"
}

# Load the configuration data
config_data = loadconfig.load_config(json_path, default_data)

# Access the configuration data
print(config_data["setting1"])
```

## Arguments

- `json_path` (Path): `pathlib.Path` pointing to the JSON file location.
- `default_data` (any, optional): Python data type (JSON compatible) to output to the JSON file. Defaults to `None`.

## Returns

- `any`: Python data type read from the JSON data.

## Sample Package Text

This program will attempt to load some of the values required to run from a file located at *~/PyAppFiles/MyApp/config.json* (sample file located in the package *json* folder). If the file isn’t found in the specified folder, the program will generate a file at that location with default values at runtime. This file’s values will need to be updated with the correct data in order for the program to run correctly, i.e., not crash.

## Sample Files

Sample `config.py` file and JSON file located in `/samples`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
