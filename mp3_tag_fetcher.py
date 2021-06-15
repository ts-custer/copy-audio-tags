# mp3_tag_fetcher.py

from argparse import ArgumentParser
from typing import Dict
import mutagen
import mutagen.flac
from tag_data import key, TagData

frame_id_mapping: Dict[str, key] = {  # 'APIC': 'PICTURE', # Picture is copied, too, but in another way
    'TCOM': key.composer,
    'TIT2': key.title,
    'TRCK': key.track_number,
    'TALB': key.album,
    'TPE1': key.artist,
    'TCON': key.genre,
    'TYER': key.date,
    'TDRC': key.date,
    'COMM': key.comment}

tag_data: TagData = TagData()


def fetch_mp3_tag(mp3_file: mutagen.File):
    frame_ids = set([s[:4] for s in mp3_file.tags.keys()])
    for frame_id in frame_ids:
        key = frame_id_mapping.get(frame_id)
        if key:
            content = mp3_file.tags.get(frame_id) and mp3_file.tags.get(frame_id).text[0]
            if content:
                tag_data.set_key_value_pair(key, content)
    fetch_picture(mp3_file)


def fetch_picture(mp3_file: mutagen.File):
    apic_list = mp3_file.tags.getall('APIC')
    if apic_list:
        first_apic = apic_list[0]
        if first_apic:
            tag_data.picture = first_apic

