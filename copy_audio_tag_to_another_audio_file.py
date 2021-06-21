#!/usr/bin/python3

"""
A script to copy all audio tags including embedded cover picture of a one audio file to another audio file.

Requires library "mutagen" (https://github.com/quodlibet/mutagen) !

Usage: copy_audio_tag_to_another_audio_file.py <source file> <target file>
"""
import os
from argparse import ArgumentParser

from flac import FlacTagWriter
from flac.flac_tag_fetcher import FlacTagFetcher
from mp3 import Mp3TagFetcher
from mp3.mp3_tag_writer import Mp3TagWriter


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
    check_if_file_exists(source_file_name)
    source_file_suffix = fetch_file_suffix(source_file_name)

    target_file_name = args.target_file
    check_if_file_exists(target_file_name)
    target_file_suffix = fetch_file_suffix(target_file_name)

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
        exit(0)

    if target_file_suffix == '.mp3':
        mp3_tag_writer = Mp3TagWriter(target_file_name)
        mp3_tag_writer.write(tag_data)
    elif target_file_suffix == '.flac':
        flac_tag_writer = FlacTagWriter(target_file_name)
        flac_tag_writer.write(tag_data)
    else:
        print(f'Not supported file type {target_file_suffix}')
        exit(0)


def check_if_file_exists(file_name: str):
    if not os.path.isfile(file_name):
        raise RuntimeError(f'File {file_name} does not exist')


def fetch_file_suffix(file_name: str) -> str:
    last_dot_index = file_name.rfind('.')
    return '' if last_dot_index == -1 else file_name[last_dot_index:].lower()


if __name__ == '__main__':
    main()
