from typing import Dict

from mutagen.id3 import TALB, TPE1, COMM, TCOM, TYER, TDRC, TCON, TIT2, TRCK


from tag_data import Key

frame_class_to_key_mapping = {  # 'APIC': Picture is loaded, too, but in another way
    TALB: Key.album,
    TPE1: Key.artist,
    COMM: Key.comment,
    TCOM: Key.composer,
    # ID3v2.3:
    TYER: Key.year,
    # ID3v2.4:
    TDRC: Key.year,
    TCON: Key.genre,
    TIT2: Key.title,
    TRCK: Key.track_number,
}

key_to_frame_class_mapping = {v: k for k, v in frame_class_to_key_mapping.items()}
# Mp3TagWriter writes ID3v2.4 tags, and frame id TDRC is right for ID3v2.4:
key_to_frame_class_mapping[Key.year] = TDRC

frame_id_to_key_mapping: Dict[str, Key] = {k.__name__: v for k, v in frame_class_to_key_mapping.items()}

key_to_frame_id_mapping: Dict[Key, str] = {v: k for k, v in frame_id_to_key_mapping.items()}

