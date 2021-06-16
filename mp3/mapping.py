from typing import Dict

from tag_data import key

frame_id_to_key_mapping: Dict[str, key] = {  # 'APIC': Picture is loaded, too, but in another way
    'TALB': key.album,
    'TPE1': key.artist,
    'COMM': key.comment,
    'TCOM': key.composer,
    'TYER': key.date,
    'TDRC': key.date,
    'TCON': key.genre,
    'TIT2': key.title,
    'TRCK': key.track_number,
}

# TODO handle 'TYER' & 'TDRC' -> key.date
key_to_frame_id_mapping: Dict[key, str] = {v: k for k,v in frame_id_to_key_mapping.items()}
