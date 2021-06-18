# mp3_tag_writer.py


import mutagen
from mutagen import flac, id3
from mutagen.mp3 import MP3
from mutagen.id3 import APIC

import tag_data
from .mapping import key_to_frame_class_mapping


class Mp3TagWriter:

    def __init__(self, mp3_file: str):
        self.mp3_file = MP3(mp3_file)

    def write(self, tag_data: tag_data.TagData):
        for key, value in tag_data.items():
            self.set_field(key, value)
        self.set_picture(tag_data.picture)
        self.mp3_file.save()

    def set_field(self, key: tag_data.Key, content: str):
        if self.mp3_file.tags is None:
            self.mp3_file.add_tags()
        frame_class = key_to_frame_class_mapping.get(key)
        self.mp3_file.tags.add(frame_class(encoding=3, text=content))

    def set_picture(self, new_picture: tag_data.Picture):
        self.mp3_file.tags.add(APIC(encoding=3, mime='image/jpeg', type=3, desc=new_picture.name, data=new_picture.data))
