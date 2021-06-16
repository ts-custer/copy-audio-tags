# flac_tag_writer.py

import mutagen

import tag_data
from .mapping import key_to_field_name_mapping


class FlacTagWriter:

    def __init__(self, flac_file: mutagen.File):
        self.flac_file: mutagen.File = flac_file

    def set_field(self, key: tag_data.key, content: str):
        field_name = key_to_field_name_mapping.get(key)
        self.flac_file[field_name] = str(content)

    def set_picture(self, type, mime, description, apic_picture_data):
        picture = mutagen.flac.Picture()
        picture.type = type
        picture.mime = mime
        picture.desc = description
        picture.data = apic_picture_data
        self.update_picture(picture)

    def update_picture(self, picture: mutagen.flac.Picture):
        self.flac_file.clear_pictures()
        self.flac_file.add_picture(picture)

    def save(self):
        self.flac_file.save()
