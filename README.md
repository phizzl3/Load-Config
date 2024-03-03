# Load-Config

Checks to see if a config json file exists at *json_path*, and returns a
python data type of the contents read from the json file. If the
json file doesn't exist, outputs json file using the python data
type (json compatible) optionally passed as *default_data*, then
loads from the file.

Args:

* json_path (Path): pathlib.Path pointing to json file location.

* default_data (any, optional): python data type (json compatible)
to output to json file. Defaults to None.

Returns:

* any: python data type read from json data.

## Usage

```py
import loadconfig

JSON = "/Volumes/USB/config.json"
_dictionary = load_config(JSON)

print(_dictionary["something cool"])
```

## Sample Package Text

This program will attempt to load some of the values required to
run from a file located at *~/PyAppFiles/MyApp/config.json* (sample
file located in package *json* folder). If the file isn’t found
in the specified folder, the program will generate a file at that
location with default values at run time. This file’s values will
need to be updated with the correct data in order for the program
to run correctly, i.e. not crash.

## Sample Files

Sample config.py file and json file located in /samples
