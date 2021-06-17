from typing import Dict

from tag_data import Key

frame_id_to_key_mapping: Dict[str, Key] = {  # 'APIC': Picture is loaded, too, but in another way
    'TALB': Key.album,
    'TPE1': Key.artist,
    'COMM': Key.comment,
    'TCOM': Key.composer,
    'TYER': Key.date,
    'TDRC': Key.date,
    'TCON': Key.genre,
    'TIT2': Key.title,
    'TRCK': Key.track_number,
}

# TODO handle 'TYER' & 'TDRC' -> key.date
key_to_frame_id_mapping: Dict[Key, str] = {v: k for k, v in frame_id_to_key_mapping.items()}
