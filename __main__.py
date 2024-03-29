#!/usr/bin/python3

from argparse import ArgumentParser
from datetime import date
from pathlib import Path

import another_mutagen_wrapper as amw
from audio_file_utils import fetch_audio_files_sorted, check_path_argument
import os

separator: str = os.sep
test_mode = False
update_comment = False
replace = ''
replace_with = ''

"""
A script to copy the audio tags including embedded cover picture of all audio files (mp3 or flac) of a directory to all
audio files (mp3 or flac) of the current working directory.

Requires https://github.com/ts-custer/another-mutagen-wrapper
"""


def main():
    # parser = ArgumentParser(prog='python3 copy-audio-tags.zip', description=__doc__)
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('source_directory',
                        type=str,
                        help='Directory with audio files to copy audio tags from')
    # Flag 'test_mode':
    parser.add_argument('-t',
                        '--test_mode',
                        help="If you set option -t ('test'), nothing will be saved",
                        action='store_true')

    # Flag 'update_comment':
    parser.add_argument('-u',
                        '--update_comment',
                        help="If you set option -u ('update comment'), "
                             "the 'comment' tag field will get the current date",
                        action='store_true')

    parser.add_argument('-r', '--replace', type=str, nargs=2, metavar=('OLD', 'NEW'),
                        help="To specify a textual replacement in the to be copied tags")

    args = parser.parse_args()

    global test_mode
    test_mode = args.test_mode
    global update_comment
    update_comment = args.update_comment
    if args.replace:
        global replace
        replace = args.replace[0]
        global replace_with
        replace_with = args.replace[1]

    # print(test_mode, update_comment, replace, replace_with)

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

    if test_mode:
        print('NOTHING SAVED BECAUSE OF TEST MODE (-t)!')


def copy_audio_tags(source_file_name: str, target_file_name: str):
    print(f'Copying audio tags from  "{source_file_name}" ---> "{target_file_name}"')

    tag_data = amw.fetch_tag_data(source_file_name)

    if update_comment:
        tag_data.update_comment(str(date.today()))

    if replace and replace_with:
        tag_data.replace_in_all_fields(replace, replace_with)

    if not test_mode:
        amw.write_tag_data_to_file(tag_data, target_file_name)


if __name__ == '__main__':
    main()
