from typing import Dict

from tag_data import Key

key_to_field_name_mapping: Dict[Key, str] = {  # field name 'PICTURE': Picture is handled in another way
    Key.album: 'ALBUM',
    Key.artist: 'ARTIST',
    Key.comment: 'DESCRIPTION',
    Key.composer: 'COMPOSER',
    Key.date: 'DATE',
    Key.genre: 'GENRE',
    Key.title: 'TITLE',
    Key.track_number: 'TRACKNUMBER',
}

field_name_to_key_mapping: Dict[str, Key] = {v: k for k, v in key_to_field_name_mapping.items()}
