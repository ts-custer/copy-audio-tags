import os
from argparse import ArgumentParser
from pathlib import Path
from typing import List

from flac import FlacTagWriter
from flac.flac_tag_fetcher import FlacTagFetcher
from mp3 import Mp3TagFetcher
from mp3.mp3_tag_writer import Mp3TagWriter

separator: str = os.sep



"""
A script to copy the audio tags including embedded cover picture of all audio files (mp3 or flac) of a directory to all
audio files (mp3 or flac) of the current working directory.

Requires library "mutagen" (https://github.com/quodlibet/mutagen)!

Usage:  copy_audio_tags <Source Directory> [-t]
        If you set option -t ('test mode'), nothing will be saved.
"""
def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('source_directory',
                        type=str,
                        help='Directory with audio files to copy audio tags from')
    args = parser.parse_args()

    target_audio_files = fetch_audio_files_sorted(Path(os.getcwd()))
    if not target_audio_files:
        print("The current directory doesn't contain any audio files!")
        exit(3)
    else:
        print(f'{len(target_audio_files)} audio files in current directory found.')

    source_directory: Path = check_path_argument(args.source_directory)
    source_audio_files = fetch_audio_files_sorted(source_directory)

    if len(source_audio_files) < len(target_audio_files):
        print(f'The source directory "{source_directory.name}" contains only {len(source_audio_files)} audio files!')
        exit(4)
    else:
        print(f'{len(source_audio_files)} audio files in the specified source directory found.')

    for index, target_audio_file in enumerate(target_audio_files):
        copy_audio_tags(source_audio_files[index], target_audio_file)


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


# The most likely file types first! Note that they all consist of four lowercase characters and that "flac" has no dot (".") intentionally.
__AUDIO_FILE_SUFFIXES = {'.mp3', 'flac'}


def is_audio_file(filename):
    lowered_last_four_characters_of_file_name = filename[-4:].lower()
    return lowered_last_four_characters_of_file_name in __AUDIO_FILE_SUFFIXES


def copy_audio_tags(source_file_name: str, target_file_name: str):
    print(f'Copying audio tags from  "{source_file_name}" ---> "{target_file_name}"')

    source_file_suffix = fetch_file_suffix(source_file_name)
    if source_file_suffix == '.mp3':
        mp3_tag_fetcher = Mp3TagFetcher(source_file_name)
        mp3_tag_fetcher.fetch_mp3_tag()
        tag_data = mp3_tag_fetcher.tag_data
    elif source_file_suffix == '.flac':
        flac_tag_fetcher = FlacTagFetcher(source_file_name)
        flac_tag_fetcher.fetch_tags()
        tag_data = flac_tag_fetcher.tag_data
    else:
        print(f'Not supported file type {source_file_suffix}')
        exit(5)

    target_file_suffix = fetch_file_suffix(target_file_name)
    if target_file_suffix == '.mp3':
        mp3_tag_writer = Mp3TagWriter(target_file_name)
        mp3_tag_writer.write(tag_data)
    elif target_file_suffix == '.flac':
        flac_tag_writer = FlacTagWriter(target_file_name)
        flac_tag_writer.write(tag_data)
    else:
        print(f'Not supported file type {target_file_suffix}')
        exit(5)


def fetch_file_suffix(file_name: str) -> str:
    last_dot_index = file_name.rfind('.')
    return '' if last_dot_index == -1 else file_name[last_dot_index:].lower()


if __name__ == '__main__':
    main()
