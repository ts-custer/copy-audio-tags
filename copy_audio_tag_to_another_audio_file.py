#!/usr/bin/python3

"""
A script to copy all audio tags including embedded cover picture of a one audio file to another audio file.

Requires https://github.com/ts-custer/another-mutagen-wrapper
and library "mutagen" https://github.com/quodlibet/mutagen.
(The latter can be installed with 'apt-get install python3-mutagen'!)

Usage: copy_audio_tag_to_another_audio_file.py <source file> <target file>
"""
from argparse import ArgumentParser

import another_mutagen_wrapper as amw
import audio_file_utils as afu


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('source_file',
                        type=str,
                        help='Name of the source audio file')
    parser.add_argument('target_file',
                        type=str,
                        help='Name of the target audio file')
    args = parser.parse_args()

    source_file_name = args.source_file
    afu.check_if_file_exists(source_file_name)

    target_file_name = args.target_file
    afu.check_if_file_exists(target_file_name)

    tag_data = amw.fetch_tag_data(source_file_name)

    amw.write_tag_data_to_file(tag_data, target_file_name)


if __name__ == '__main__':
    main()
