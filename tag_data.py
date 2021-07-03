# tag_data.py
from datetime import date
from enum import Enum
from typing import Dict


# Supported audio file types
AUDIO_FILE_SUFFIXES = {'.mp3', '.flac'}

# Supported tag fields
Key = Enum('Key', 'album artist comment composer genre title track_number year')


class Picture:

    def __init__(self, name: str, data: bytes):
        self._name: str = name
        self._data: bytes = data

    @property
    def data(self):
        return self._data

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        if isinstance(other, Picture):
            return self._name == other._name and self._data == other._data
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self._name, self._data))

    def __str__(self):
        return f'Picture "{self._name}": {self._data}'


class TagData:

    def __init__(self):
        self._key_value_mapping: Dict[Key, str] = {}
        self._picture = None

    def set_key_value_pair(self, key: Key, value: str):
        self._key_value_mapping[key] = str(value)

    def get_value_by_key(self, key: Key) -> str:
        return self._key_value_mapping.get(key, '')

    def items(self):
        return self._key_value_mapping.items()

    @property
    def picture(self) -> Picture:
        return self._picture

    @picture.setter
    def picture(self, picture: Picture):
        self._picture = picture

    def pprint(self):
        for key, value in self._key_value_mapping.items():
            print(f"{key}: {value}")
        print(f'{self._picture}')

    def __eq__(self, other):
        if isinstance(other, TagData):
            return self._key_value_mapping == other._key_value_mapping and self._picture == other._picture
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self._key_value_mapping, self._picture))

    def __str__(self):
        return 'TagData (' + str(self._key_value_mapping) + ', ' + str(self._picture) + ')'

    def update_comment(self):
        self.set_key_value_pair(Key.comment, str(date.today()))

    def replace(self, replace: str, replace_with: str):
        self._key_value_mapping = {
            key: content.replace(replace, replace_with)
            for key, content in self._key_value_mapping.items()
        }


def check_and_fetch_file_suffix(file_name: str) -> str:
    last_dot_index = file_name.rfind('.')
    file_suffix = file_name[last_dot_index:].lower()
    if file_suffix not in AUDIO_FILE_SUFFIXES:
        print(f'Not supported file type {file_suffix}\n{file_name}')
        exit(1)
    else:
        return file_suffix
