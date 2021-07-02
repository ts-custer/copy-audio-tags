# file_utils.py

import os
from pathlib import Path
from typing import List

separator: str = os.sep

def check_path_argument(path_argument: str) -> Path:
    possible_directory: Path = Path(path_argument)
    if not possible_directory.exists():
        print("Directory '{}' does not exist".format(path_argument))
        exit(1)
    if not possible_directory.is_dir():
        print("'{}' is not a directory".format(path_argument))
        exit(2)
    return possible_directory


def fetch_audio_files_sorted(directory: Path) -> List[str]:
    directory_name = str(directory) + separator
    audio_file_list = []
    for file_or_directory in directory.iterdir():
        if file_or_directory.is_file() and is_audio_file(file_or_directory.name):
            audio_file_list.append(directory_name + file_or_directory.name)
    return sorted(audio_file_list)


# Note that they consist of four lowercase characters and that "flac" has no dot (".") intentionally.
__AUDIO_FILE_SUFFIXES = {'.mp3', 'flac'}


def is_audio_file(filename):
    lowered_last_four_characters_of_file_name = filename[-4:].lower()
    return lowered_last_four_characters_of_file_name in __AUDIO_FILE_SUFFIXES


def fetch_file_suffix(file_name: str) -> str:
    last_dot_index = file_name.rfind('.')
    return '' if last_dot_index == -1 else file_name[last_dot_index:].lower()
