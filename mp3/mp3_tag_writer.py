# mp3_tag_writer.py


from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import APIC

from tag_data import TagData, Key, Picture
from .mapping import key_to_frame_class_mapping


def delete_mp3_tags(mp3_full_file_name: str):
    mp3_file = EasyID3(mp3_full_file_name)
    mp3_file.delete()
    mp3_file.save()


class Mp3TagWriter:

    def __init__(self, mp3_file: str):
        self.mp3_file = MP3(mp3_file)

    def write(self, tag_data: TagData):
        for key, value in tag_data.items():
            self.set_field(key, value)
        if tag_data.picture:
            self.set_picture(tag_data.picture)
        self.mp3_file.save()

    def set_field(self, key: Key, content: str):
        if self.mp3_file.tags is None:
            self.mp3_file.add_tags()
        frame_class = key_to_frame_class_mapping.get(key)
        self.mp3_file.tags.add(frame_class(encoding=3, text=content))

    def set_picture(self, new_picture: Picture):
        self.mp3_file.tags.add(APIC(encoding=3,
                                    mime='image/jpeg',
                                    type=3, desc=new_picture.name,
                                    data=new_picture.data))
