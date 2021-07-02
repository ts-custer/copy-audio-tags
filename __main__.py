#!/usr/bin/python3

import os
from argparse import ArgumentParser
from pathlib import Path
from file_utils import *

from flac import FlacTagWriter, delete_flac_tags
from flac.flac_tag_fetcher import FlacTagFetcher
from mp3 import Mp3TagFetcher
from mp3.mp3_tag_writer import Mp3TagWriter, delete_mp3_tags

separator: str = os.sep
test_mode = False
update_comment = False
replace = ''
replace_with = ''

"""
A script to copy the audio tags including embedded cover picture of all audio files (mp3 or flac) of a directory to all
audio files (mp3 or flac) of the current working directory.

Requires library "mutagen" (https://github.com/quodlibet/mutagen)!
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

    if update_comment:
        tag_data.update_comment()

    if replace and replace_with:
        tag_data.replace(replace, replace_with)

    target_file_suffix = fetch_file_suffix(target_file_name)
    if target_file_suffix == '.mp3':
        delete_mp3_tags(target_file_name)
        mp3_tag_writer = Mp3TagWriter(target_file_name)
        if not test_mode:
            mp3_tag_writer.write(tag_data)
    elif target_file_suffix == '.flac':
        delete_flac_tags(target_file_name)
        flac_tag_writer = FlacTagWriter(target_file_name)
        if not test_mode:
            flac_tag_writer.write(tag_data)
    else:
        print(f'Not supported file type {target_file_suffix}')
        exit(5)


if __name__ == '__main__':
    main()
