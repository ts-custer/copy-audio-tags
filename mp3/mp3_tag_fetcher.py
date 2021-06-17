# mp3_tag_fetcher.py

import mutagen.flac

from .mapping import frame_id_to_key_mapping
from tag_data import TagData, Picture


class Mp3TagFetcher:

    def __init__(self, mp3_file: mutagen.File):
        self._tag_data: TagData = None
        self.mp3_file = mp3_file

    def fetch_mp3_tag(self):
        self._tag_data = TagData()
        frame_ids = set([s[:4] for s in self.mp3_file.tags.keys()])
        for frame_id in frame_ids:
            key = frame_id_to_key_mapping.get(frame_id)
            if key:
                content = self.mp3_file.tags.get(frame_id) and self.mp3_file.tags.get(frame_id).text[0]
                if content:
                    self._tag_data.set_key_value_pair(key, content)
        self.fetch_picture()

    def fetch_picture(self):
        apic_list = self.mp3_file.tags.getall('APIC')
        if apic_list:
            first_apic = apic_list[0]
            if first_apic:
                self._tag_data.picture = Picture(first_apic.desc, first_apic.data)

    @property
    def tag_data(self):
        return self._tag_data


