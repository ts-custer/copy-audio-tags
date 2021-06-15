import os
import unittest

import mutagen

import mp3_tag_fetcher
from tag_data import key


class Id3v1FetcherTest(unittest.TestCase):

    def setUp(self) -> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        full_filename = dir_path + '/fixtures/id3v1.mp3'
        mp3_file = mutagen.File(full_filename)
        mp3_tag_fetcher.fetch_mp3_tag(mp3_file)


    def test(self):
        # mp3_tag_fetcher.tag_data.pprint()
        self.assertEqual('id3v1 album', mp3_tag_fetcher.tag_data.get_value_by_key(key.album))
        self.assertEqual('id3v1 artist', mp3_tag_fetcher.tag_data.get_value_by_key(key.artist))
        self.assertEqual('2020', mp3_tag_fetcher.tag_data.get_value_by_key(key.date))
        self.assertEqual('7', mp3_tag_fetcher.tag_data.get_value_by_key(key.track_number))
        self.assertEqual('id3v1 title', mp3_tag_fetcher.tag_data.get_value_by_key(key.title))
        self.assertEqual('Rock & Roll', mp3_tag_fetcher.tag_data.get_value_by_key(key.genre))
        self.assertIsNone(mp3_tag_fetcher.tag_data.picture)


class Id3v23FetcherTest(unittest.TestCase):

    def setUp(self) -> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        full_filename = dir_path + '/fixtures/id3v2.3.mp3'
        mp3_file = mutagen.File(full_filename)
        mp3_tag_fetcher.fetch_mp3_tag(mp3_file)

    def test(self):
        mp3_tag_fetcher.tag_data.pprint()


class Id3v24FetcherTest(unittest.TestCase):

    def setUp(self) -> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        full_filename = dir_path + '/fixtures/id3v2.4.mp3'
        mp3_file = mutagen.File(full_filename)
        mp3_tag_fetcher.fetch_mp3_tag(mp3_file)

    def test(self):
        mp3_tag_fetcher.tag_data.pprint()


if __name__ == '__main__':
    unittest.main()
