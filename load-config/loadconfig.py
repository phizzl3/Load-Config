__version__ = "1.1.0"

import json
import time
from pathlib import Path
from typing import Any, Optional


def load_config(json_path: Path, default_data: Optional[Any] = None) -> Any:
    json_path = __verify_path_object(json_path)
    __verify_or_write_json(json_path, default_data)
    return __load_data_from_json(json_path)


def __verify_path_object(json_path: Path) -> Path:
    if not isinstance(json_path, Path):
        json_path = Path(json_path)
    return json_path


def __write_default_data(json_path: Path, default_data: Any) -> None:
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(default_data, json_file, indent=2)


def __verify_or_write_json(json_path: Path, default_data: Optional[Any] = None) -> None:
    if not json_path.exists():
        if not json_path.parent.is_dir():
            json_path.parent.mkdir(parents=True)

        if default_data:
            __write_default_data(json_path, default_data)
        else:
            print(f"\n File not found:\n {json_path}")
            time.sleep(5)


def __load_data_from_json(json_path: Path) -> Any:
    with open(json_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)
