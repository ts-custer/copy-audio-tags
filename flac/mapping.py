from typing import Dict

from tag_data import key

key_to_field_name_mapping: Dict[key, str] = {  # field name 'PICTURE': Picture is handled in another way
    key.album: 'ALBUM',
    key.artist: 'ARTIST',
    key.comment: 'DESCRIPTION',
    key.composer: 'COMPOSER',
    key.date: 'DATE',
    key.genre: 'GENRE',
    key.title: 'TITLE',
    key.track_number: 'TRACKNUMBER',
}

field_name_to_key_mapping: Dict[str, key] = {v: k for k,v in key_to_field_name_mapping.items()}
