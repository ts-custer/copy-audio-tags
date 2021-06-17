# test_flag_tag_writer.py
import os
import unittest

import mutagen
from flac import FlacTagWriter
from tag_data import Key, TagData

fixtures_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/fixtures/'


class FlacTagWriterTest(unittest.TestCase):

    def setUp(self) -> None:
        self.empty_flac_file = mutagen.File(fixtures_directory_path + 'empty_flac.flac')
        self.reset_flac_file()
        self.flac_tag_writer = FlacTagWriter(self.empty_flac_file)
        self.flac_tag_writer.set_field(Key.album, 'test album')
        self.flac_tag_writer.set_field(Key.artist, 'test artist')
        self.flac_tag_writer.set_field(Key.comment, 'test comment')
        self.flac_tag_writer.set_field(Key.composer, 'test composer')
        self.flac_tag_writer.set_field(Key.date, '2021')
        self.flac_tag_writer.set_field(Key.genre, 'test genre')
        self.flac_tag_writer.set_field(Key.title, 'test title')
        self.flac_tag_writer.set_field(Key.track_number, '01/17')

        picture_file_name = 'flac.jpg'
        self.picture_full_filename = fixtures_directory_path + picture_file_name
        with open(self.picture_full_filename, "rb") as f:
            picture_data = f.read()
        self.flac_tag_writer.set_picture(picture_file_name, picture_data)
        self.flac_tag_writer.save()

    def tearDown(self) -> None:
        self.reset_flac_file()
        pass

    def reset_flac_file(self):
        self.empty_flac_file.delete()
        self.empty_flac_file.clear_pictures()
        self.empty_flac_file.save()

    def test(self):
        self.assertEqual('test album', self.empty_flac_file.get('ALBUM')[0])
        self.assertEqual('test artist', self.empty_flac_file.get('ARTIST')[0])
        self.assertEqual('test comment', self.empty_flac_file.get('DESCRIPTION')[0])
        self.assertEqual('test composer', self.empty_flac_file.get('COMPOSER')[0])
        self.assertEqual('2021', self.empty_flac_file.get('DATE')[0])
        self.assertEqual('test genre', self.empty_flac_file.get('GENRE')[0])
        self.assertEqual('test title', self.empty_flac_file.get('TITLE')[0])
        self.assertEqual('01/17', self.empty_flac_file.get('TRACKNUMBER')[0])

        embedded_picture = self.empty_flac_file.pictures[0]
        with open(self.picture_full_filename, "rb") as f:
            picture_data = f.read()
        self.assertEqual(picture_data, embedded_picture.data)


if __name__ == '__main__':
    unittest.main()
