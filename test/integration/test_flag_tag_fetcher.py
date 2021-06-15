import os
import unittest

from flac_tag_fetcher import FlacTagFetcher


class FlacTagFetcherTest(unittest.TestCase):

    def setUp(self) -> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        full_filename = dir_path + '/fixtures/flac.flac'
        self.flag_tag_fetcher = FlacTagFetcher(full_filename)

    def test_flac_exists(self):
        self.assertTrue(self.flag_tag_fetcher.flac_exists)

    def test_contains_image(self):
        self.assertTrue(self.flag_tag_fetcher.contains_image())

    def test_fetch_album(self):
        self.assertEqual("flac album", self.flag_tag_fetcher.fetch_album())

    def test_fetch_title(self):
        self.assertEqual("flac title", self.flag_tag_fetcher.fetch_title())

    def test_fetch_year(self):
        self.assertEqual("2023", self.flag_tag_fetcher.fetch_year())

    def test_fetch_artist(self):
        self.assertEqual("flac artist", self.flag_tag_fetcher.fetch_artist())

    def test_fetch_track_number(self):
        self.assertEqual("10", self.flag_tag_fetcher.fetch_track_number())

    def test_fetch_genre(self):
        self.assertEqual("flac genre", self.flag_tag_fetcher.fetch_genre())

    def test_fetch_comment(self):
        self.assertEqual("flac comment", self.flag_tag_fetcher.fetch_comment())


if __name__ == '__main__':
    unittest.main()
