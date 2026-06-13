# Load-Config

Load-Config is a Python utility that loads JSON configuration data and creates the file automatically with default values when it does not exist. It also writes a helper `README.txt` alongside the generated JSON file to explain the configuration purpose.

## Repository Layout

- `load-config/loadconfig.py`: Main loader implementation.
- `load-config/configuration.py`: Sample module showing how to import and use `load_config`.
- `sample/config.json`: Sample JSON configuration file.
- `README.md`: Project documentation.

## Features

- Load configuration data from a JSON file.
- Automatically create a missing JSON file using provided default data.
- Generate a companion `README.txt` in the configuration folder with usage instructions.
- Works with Python standard library only.

## Installation

Clone the repository. No external dependencies are required.

```sh
git clone https://github.com/yourusername/Load-Config.git
cd Load-Config
```

## Getting Started

1. Open a terminal in the repository root.
2. Run the sample configuration module from the `load-config` folder:

```sh
cd load-config
python configuration.py
```

3. If the configured JSON file does not exist, `load_config()` will create it with default values and write a companion `README.txt` in the same folder.
4. Edit the generated JSON file to update your settings, then rerun the sample module or import `load_config` from your own application.

To use the loader directly from the `load-config` module, either run from that directory or include it on `PYTHONPATH`.

```sh
cd load-config
python -c "from loadconfig import load_config; from pathlib import Path; print(load_config(Path('sample/config.json')) )"
```

Or from the repository root:

```sh
PYTHONPATH=./load-config python -c "from loadconfig import load_config; from pathlib import Path; print(load_config(Path('sample/config.json')) )"
```

## Usage

```py
from pathlib import Path
from loadconfig import load_config

json_path = Path.home() / 'PyAppFiles' / 'My Application' / 'config.json'

default_data = {
    'random number': 20,
    'working folder name': 'My Folder',
    'output file name': 'Output.txt',
}

config_data = load_config(json_path, default_data=default_data)
print(config_data['random number'])
```

## Behavior

- If the JSON file exists, `load_config()` reads and returns the contents.
- If the JSON file is missing and `default_data` is provided, the function creates the file and writes the default data.
- If the JSON file is missing, `load_config()` also creates `README.txt` in the same folder to explain how to update the generated configuration.

## Sample Files

- `load-config/configuration.py`: Example sample module that loads JSON configuration and builds a `CONFIG` dictionary.
- `sample/config.json`: Example configuration file with default values.

## Notes

The loader is implemented as a plain module in `load-config/loadconfig.py`, so import it as `from loadconfig import load_config` when `load-config/` is available on your Python path.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
