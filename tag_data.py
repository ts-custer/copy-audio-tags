# tag_data.py

from enum import Enum
from typing import Dict, Any


Key = Enum('Key', 'artist title album track_number genre date comment composer')


class TagData:

    def __init__(self):
        self._key_value_mapping: Dict[Key, str] = {}
        self._picture: bytes = None

    def set_key_value_pair(self, key: Key, value: str):
        self._key_value_mapping[key] = str(value)

    def get_value_by_key(self, key: Key) -> str:
        return self._key_value_mapping.get(key, '')

    @property
    def key_value_mapping(self):
        return self._key_value_mapping

    @property
    def picture(self) -> bytes:
        return self._picture

    @picture.setter
    def picture(self, picture: bytes):
        self._picture = picture

    def pprint(self):
        for key, value in self._key_value_mapping.items():
            print(f"{key}: {value}")
        print(f"picture: {self._picture}")


