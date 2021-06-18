from typing import Dict

from mutagen.id3 import TALB, TPE1, COMM, TCOM, TYER, TDRC, TCON, TIT2, TRCK


from tag_data import Key

frame_class_to_key_mapping = {  # 'APIC': Picture is loaded, too, but in another way
    TALB: Key.album,
    TPE1: Key.artist,
    COMM: Key.comment,
    TCOM: Key.composer,
    TYER: Key.year,
    TDRC: Key.year,
    TCON: Key.genre,
    TIT2: Key.title,
    TRCK: Key.track_number,
}

# TODO handle 'TYER' & 'TDRC' -> key.year
key_to_frame_class_mapping = {v: k for k, v in frame_class_to_key_mapping.items()}

frame_id_to_key_mapping: Dict[str, Key] = {k.__name__: v for k, v in frame_class_to_key_mapping.items()}

key_to_frame_id_mapping: Dict[Key, str] = {v: k for k, v in frame_id_to_key_mapping.items()}

