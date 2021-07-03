# audio_tag_fetcher.py
from flac.flac_tag_fetcher import FlacTagFetcher
from mp3 import Mp3TagFetcher
from tag_data import check_and_fetch_file_suffix


class AudioTagFetcher:

    def __init__(self):
        self._tag_data = None

    def fetch_tag(self, audio_file: str):
        self._tag_data = None
        file_suffix = check_and_fetch_file_suffix(audio_file)
        if file_suffix == '.mp3':
            mp3_tag_fetcher = Mp3TagFetcher(audio_file)
            mp3_tag_fetcher.fetch_mp3_tag()
            self._tag_data = mp3_tag_fetcher.tag_data
        elif file_suffix == '.flac':
            flac_tag_fetcher = FlacTagFetcher(audio_file)
            flac_tag_fetcher.fetch_tags()
            self._tag_data = flac_tag_fetcher.tag_data

    @property
    def tag_data(self):
        return self._tag_data
