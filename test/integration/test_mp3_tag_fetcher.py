import os
import unittest

import mutagen

from mp3 import Mp3TagFetcher
from tag_data import Key


fixtures_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/fixtures/'


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
        mp3_file = mutagen.File(fixtures_directory_path + 'id3v2.3.mp3')
        self.mp3_tag_fetcher = Mp3TagFetcher(mp3_file)
        self.mp3_tag_fetcher.fetch_mp3_tag()

    def test(self):
        self.assertEqual('id3v2.3 album', self.mp3_tag_fetcher.tag_data.get_value_by_key(Key.album))
        self.assertEqual('id3v2.3 artist', self.mp3_tag_fetcher.tag_data.get_value_by_key(Key.artist))
        self.assertEqual('2021', self.mp3_tag_fetcher.tag_data.get_value_by_key(Key.date))
        self.assertEqual('08/11', self.mp3_tag_fetcher.tag_data.get_value_by_key(Key.track_number))
        self.assertEqual('id3v2.3 title', self.mp3_tag_fetcher.tag_data.get_value_by_key(Key.title))
        self.assertEqual('id3v2.3 genre', self.mp3_tag_fetcher.tag_data.get_value_by_key(Key.genre))
        self.assertEqual('id3v2.3 composer', self.mp3_tag_fetcher.tag_data.get_value_by_key(Key.composer))
        self.assertIsNotNone(self.mp3_tag_fetcher.tag_data.picture)

        picture_full_filename = fixtures_directory_path + 'id3v2.3.jpg'
        with open(picture_full_filename, "rb") as f:
            picture_data = f.read()
        self.assertEqual(picture_data, self.mp3_tag_fetcher.tag_data.picture.data)


class Id3v24FetcherTest(unittest.TestCase):

    def setUp(self) -> None:
        mp3_file = mutagen.File(fixtures_directory_path + 'id3v2.4.mp3')
        self.mp3_tag_fetcher = Mp3TagFetcher(mp3_file)
        self.mp3_tag_fetcher.fetch_mp3_tag()

    def test(self):
        self.assertEqual('id3v2.4 album', self.mp3_tag_fetcher.tag_data.get_value_by_key(Key.album))
        self.assertEqual('id3v2.4 artist', self.mp3_tag_fetcher.tag_data.get_value_by_key(Key.artist))
        self.assertEqual('2022', self.mp3_tag_fetcher.tag_data.get_value_by_key(Key.date))
        self.assertEqual('09/12', self.mp3_tag_fetcher.tag_data.get_value_by_key(Key.track_number))
        self.assertEqual('id3v2.4 title', self.mp3_tag_fetcher.tag_data.get_value_by_key(Key.title))
        self.assertEqual('id3v2.4 genre', self.mp3_tag_fetcher.tag_data.get_value_by_key(Key.genre))
        self.assertEqual('id3v2.4 composer', self.mp3_tag_fetcher.tag_data.get_value_by_key(Key.composer))
        self.assertIsNotNone(self.mp3_tag_fetcher.tag_data.picture)

        picture_full_filename = fixtures_directory_path + 'id3v2.4.jpg'
        with open(picture_full_filename, "rb") as f:
            picture_data = f.read()
        self.assertEqual(picture_data, self.mp3_tag_fetcher.tag_data.picture.data)


if __name__ == '__main__':
    unittest.main()
