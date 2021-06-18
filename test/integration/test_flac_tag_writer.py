# test_flag_tag_writer.py
import os
import unittest

import mutagen
from flac import FlacTagWriter
from tag_data import Key, TagData, Picture

fixtures_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/fixtures/'
flac_file_name = 'empty_flac.flac'


class FlacTagWriterTest(unittest.TestCase):

    def setUp(self) -> None:
        self.reset_flac_file()
        tag_data = TagData()
        tag_data.set_key_value_pair(Key.album, 'test album')
        tag_data.set_key_value_pair(Key.artist, 'test artist')
        tag_data.set_key_value_pair(Key.comment, 'test comment')
        tag_data.set_key_value_pair(Key.composer, 'test composer')
        tag_data.set_key_value_pair(Key.genre, 'test genre')
        tag_data.set_key_value_pair(Key.title, 'test title')
        tag_data.set_key_value_pair(Key.track_number, '01/17')
        tag_data.set_key_value_pair(Key.year, '2021')

        picture_file_name = 'flac.jpg'
        self.picture_full_filename = fixtures_directory_path + picture_file_name
        with open(self.picture_full_filename, "rb") as f:
            picture_data = f.read()
        tag_data.picture = Picture(picture_file_name, picture_data)
        FlacTagWriter(fixtures_directory_path + flac_file_name).write(tag_data)

    def tearDown(self) -> None:
        self.reset_flac_file()
        pass

    def reset_flac_file(self):
        flac_file = mutagen.File(fixtures_directory_path + flac_file_name)
        flac_file.delete()
        flac_file.clear_pictures()
        flac_file.save()

    def test(self):
        flac_file = mutagen.File(fixtures_directory_path + flac_file_name)
        self.assertEqual('test album', flac_file.get('ALBUM')[0])
        self.assertEqual('test artist', flac_file.get('ARTIST')[0])
        self.assertEqual('test comment', flac_file.get('DESCRIPTION')[0])
        self.assertEqual('test composer', flac_file.get('COMPOSER')[0])
        self.assertEqual('2021', flac_file.get('DATE')[0])
        self.assertEqual('test genre', flac_file.get('GENRE')[0])
        self.assertEqual('test title', flac_file.get('TITLE')[0])
        self.assertEqual('01/17', flac_file.get('TRACKNUMBER')[0])

        embedded_picture = flac_file.pictures[0]
        with open(self.picture_full_filename, "rb") as f:
            picture_data = f.read()
        self.assertEqual(picture_data, embedded_picture.data)


if __name__ == '__main__':
    unittest.main()
