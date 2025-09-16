#!/usr/bin/env python3
"""
Author: Greg Chetcuti <greg@greg.ca>
Date: 2021-08-13
Purpose: Move the contents of one folder to another
"""

import configparser
import pathlib
import shutil

config = configparser.ConfigParser()
config.read(str(pathlib.Path(__file__).absolute())[:-2] + "ini")

source_dir = config["config"]["source_dir"]
target_dir = config["config"]["target_dir"]


# =============================================================================
# Main                                                                     Main
# ----------------------------------------------------------
def main():
    """Run the main program"""
    for item in pathlib.Path(source_dir).iterdir():
        dest_path = pathlib.Path(target_dir) / item.name
        dest_path = get_unique_path(dest_path)
        shutil.move(str(item), str(dest_path))

def get_unique_path(dest_path):
    counter = 1
    stem = dest_path.stem
    suffix = dest_path.suffix
    while dest_path.exists():
        dest_path = dest_path.with_name(f"{stem}_{counter}{suffix}")
        counter += 1
    return dest_path

# ----------------------------------------------------------
if __name__ == "__main__":
    main()

