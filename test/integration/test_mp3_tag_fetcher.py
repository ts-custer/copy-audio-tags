import os
import unittest

import mutagen

from mp3 import Mp3TagFetcher
from tag_data import Key, TagData, Picture

fixtures_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/fixtures/'


# TODO implement and use
def initiate_tag_data(id3_subversion: str) -> TagData:
    tag_data = TagData()
    id3version = f'id3v2.{id3_subversion}'
    tag_data.set_key_value_pair(Key.album, f'id3v2.{id3_subversion} album')
    tag_data.set_key_value_pair(Key.artist, 'id3v2.3 artist')
    # TODO comment can't be loaded from mp3!
    # tag_data.set_key_value_pair(Key.comment, 'id3v2.3 comment')
    tag_data.set_key_value_pair(Key.composer, 'id3v2.3 composer')
    tag_data.set_key_value_pair(Key.genre, 'id3v2.3 genre')
    tag_data.set_key_value_pair(Key.title, 'id3v2.3 title')
    tag_data.set_key_value_pair(Key.track_number, '08/11')
    tag_data.set_key_value_pair(Key.year, '2021')
    picture_name = 'id3v2.3.jpg'
    with open(fixtures_directory_path + picture_name, "rb") as f:
        picture_data = f.read()
    tag_data.picture = Picture(picture_name, picture_data)
    return tag_data


# class Id3v1FetcherTest(unittest.TestCase):
#
#     def setUp(self) -> None:
#         dir_path = os.path.dirname(os.path.realpath(__file__))
#         full_filename = dir_path + '/fixtures/id3v1.mp3'
#         mp3_file = mutagen.File(full_filename)
#         mp3_tag_fetcher.fetch_mp3_tag(mp3_file)
#
#
#     def test(self):
#         # mp3_tag_fetcher.tag_data.pprint()
#         self.assertEqual('id3v1 album', mp3_tag_fetcher.tag_data.get_value_by_key(key.album))
#         self.assertEqual('id3v1 artist', mp3_tag_fetcher.tag_data.get_value_by_key(key.artist))
#         self.assertEqual('2020', mp3_tag_fetcher.tag_data.get_value_by_key(key.date))
#         self.assertEqual('7', mp3_tag_fetcher.tag_data.get_value_by_key(key.track_number))
#         self.assertEqual('id3v1 title', mp3_tag_fetcher.tag_data.get_value_by_key(key.title))
#         self.assertEqual('Rock & Roll', mp3_tag_fetcher.tag_data.get_value_by_key(key.genre))
#         self.assertIsNone(mp3_tag_fetcher.tag_data.picture)


class Id3v23FetcherTest(unittest.TestCase):

    def setUp(self) -> None:
        self.expected_tag_data = TagData()
        self.expected_tag_data.set_key_value_pair(Key.album, 'id3v2.3 album')
        self.expected_tag_data.set_key_value_pair(Key.artist, 'id3v2.3 artist')
        self.expected_tag_data.set_key_value_pair(Key.comment, 'id3v2.3 comment')
        self.expected_tag_data.set_key_value_pair(Key.composer, 'id3v2.3 composer')
        self.expected_tag_data.set_key_value_pair(Key.genre, 'id3v2.3 genre')
        self.expected_tag_data.set_key_value_pair(Key.title, 'id3v2.3 title')
        self.expected_tag_data.set_key_value_pair(Key.track_number, '08/11')
        self.expected_tag_data.set_key_value_pair(Key.year, '2021')
        picture_name = 'id3v2.3.jpg'
        with open(fixtures_directory_path + picture_name, "rb") as f:
            picture_data = f.read()
        self.expected_tag_data.picture = Picture(picture_name, picture_data)

    def test(self):
        mp3_file = mutagen.File(fixtures_directory_path + 'id3v2.3.mp3')
        mp3_tag_fetcher = Mp3TagFetcher(mp3_file)
        mp3_tag_fetcher.fetch_mp3_tag()
        self.assertEqual(self.expected_tag_data, mp3_tag_fetcher.tag_data)


class Id3v24FetcherTest(unittest.TestCase):

    def setUp(self) -> None:
        self.expected_tag_data = TagData()
        self.expected_tag_data.set_key_value_pair(Key.album, 'id3v2.4 album')
        self.expected_tag_data.set_key_value_pair(Key.artist, 'id3v2.4 artist')
        self.expected_tag_data.set_key_value_pair(Key.comment, 'id3v2.4 comment')
        self.expected_tag_data.set_key_value_pair(Key.composer, 'id3v2.4 composer')
        self.expected_tag_data.set_key_value_pair(Key.genre, 'id3v2.4 genre')
        self.expected_tag_data.set_key_value_pair(Key.title, 'id3v2.4 title')
        self.expected_tag_data.set_key_value_pair(Key.track_number, '09/12')
        self.expected_tag_data.set_key_value_pair(Key.year, '2022')
        picture_name = 'id3v2.4.jpg'
        with open(fixtures_directory_path + picture_name, "rb") as f:
            picture_data = f.read()
        self.expected_tag_data.picture = Picture(picture_name, picture_data)

    def test(self):
        mp3_file = mutagen.File(fixtures_directory_path + 'id3v2.4.mp3')
        mp3_tag_fetcher = Mp3TagFetcher(mp3_file)
        mp3_tag_fetcher.fetch_mp3_tag()
        self.assertEqual(self.expected_tag_data, mp3_tag_fetcher.tag_data)


if __name__ == '__main__':
    unittest.main()
