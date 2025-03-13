"""
This module provides functionality to load and manage JSON configuration files.
It includes functions to verify paths, write default data, and load data from JSON files.
"""

__version__ = "1.2.0"

import json
import time
from pathlib import Path
from typing import Any, Optional


def load_config(json_path: Path, default_data: Optional[Any] = None) -> Any:
    """
    Load configuration data from a JSON file. If the file does not exist, it will be created with default data.

    Args:
        json_path (Path): The path to the JSON file.
        default_data (Optional[Any]): The default data to write if the file does not exist.

    Returns:
        Any: The data loaded from the JSON file.
    """
    json_path = __verify_path_object(json_path)
    __verify_or_write_json(json_path, default_data)
    return __load_data_from_json(json_path)


def __verify_path_object(json_path: Path) -> Path:
    """
    Verify that the given path is a Path object. If not, convert it to a Path object.

    Args:
        json_path (Path): The path to verify.

    Returns:
        Path: The verified Path object.
    """
    if not isinstance(json_path, Path):
        json_path = Path(json_path)
    return json_path


def __write_default_data(json_path: Path, default_data: Any) -> None:
    """
    Write default data to a JSON file.

    Args:
        json_path (Path): The path to the JSON file.
        default_data (Any): The default data to write.
    """
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(default_data, json_file, indent=2)


def __verify_or_write_json(json_path: Path, default_data: Optional[Any] = None) -> None:
    """
    Verify if a JSON file exists. If not, create the file with default data or print a file not found message.

    Args:
        json_path (Path): The path to the JSON file.
        default_data (Optional[Any]): The default data to write if the file does not exist.
    """
    if not json_path.exists():
        if not json_path.parent.is_dir():
            json_path.parent.mkdir(parents=True)

        if default_data:
            __write_default_data(json_path, default_data)
        else:
            print(f"\n File not found:\n {json_path}")
            time.sleep(5)


def __load_data_from_json(json_path: Path) -> Any:
    """
    Load data from a JSON file.

    Args:
        json_path (Path): The path to the JSON file.

    Returns:
        Any: The data loaded from the JSON file.
    """
    with open(json_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)
