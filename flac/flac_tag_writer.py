# flac_tag_writer.py

import mutagen
from mutagen import flac, id3

import tag_data
from .mapping import key_to_field_name_mapping


def delete_flac_tags(flac_full_file_name: str):
    flac_file = mutagen.File(flac_full_file_name)
    flac_file.delete()
    flac_file.clear_pictures()
    flac_file.save()


class FlacTagWriter:

    def __init__(self, flac_file: str):
        self.flac_file = mutagen.File(flac_file)

    def write(self, tag_data: tag_data.TagData):
        for key, value in tag_data.items():
            self.set_field(key, value)
        if tag_data.picture:
            self.set_picture(tag_data.picture)
        self.save()

    def set_field(self, key: tag_data.Key, content: str):
        field_name = key_to_field_name_mapping.get(key)
        self.flac_file[field_name] = str(content)

    def set_picture(self, new_picture: tag_data.Picture):
        picture = mutagen.flac.Picture()
        picture.type = id3.PictureType.COVER_FRONT
        picture.mime = 'image/jpeg'
        picture.desc = new_picture.name
        picture.data = new_picture.data
        self.update_picture(picture)

    def update_picture(self, picture: mutagen.flac.Picture):
        self.flac_file.clear_pictures()
        self.flac_file.add_picture(picture)

    def save(self):
        self.flac_file.save()
