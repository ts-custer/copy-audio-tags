# tag_data.py

from enum import Enum
from typing import Dict, Any


key = Enum('Key', 'artist title album track_number genre date comment composer')


class TagData:

    def __init__(self):
        self._key_value_mapping: Dict[key, str] = {}
        self._picture = None

    def set_key_value_pair(self, key: key, value: str):
        self._key_value_mapping[key] = str(value)

    def get_value_by_key(self, key: key) -> str:
        return self._key_value_mapping.get(key, '')

    @property
    def picture(self):
        return self._picture

    @picture.setter
    def picture(self, picture):
        self._picture = picture

    def pprint(self):
        for key, value in self._key_value_mapping.items():
            print(f"{key}: {value}")
        print(f"picture: {self._picture}")


