# tryout.py
import mutagen

from flac.flac_tag_fetcher import FlacTagFetcher
from mp3 import Mp3TagFetcher


# mp3_file = mutagen.File('/home/thees/PycharmProjects/copy-audio-tag-to-another-audio-file/test/integration/fixtures/id3v2.3.mp3')
# mp3_tag_fetcher = Mp3TagFetcher(mp3_file)
# mp3_tag_fetcher.fetch_mp3_tag()

# from mutagen.easyid3 import EasyID3
# print(EasyID3.valid_keys.keys())

############################

# from mp3.mp3_tag_writer import Mp3TagWriter
# from tag_data import TagData, Key, Picture
#
# mp3_file_name = '/home/thees/PycharmProjects/copy-audio-tag-to-another-audio-file/test/integration/fixtures/empty_mp3.mp3'
#
# tag_data = TagData()
# tag_data.set_key_value_pair(Key.album, 'album')
# tag_data.set_key_value_pair(Key.artist, 'artist')
# tag_data.set_key_value_pair(Key.comment, 'comment')
# tag_data.set_key_value_pair(Key.composer, 'composer')
# tag_data.set_key_value_pair(Key.genre, 'genre')
# tag_data.set_key_value_pair(Key.title, 'title')
# tag_data.set_key_value_pair(Key.track_number, '03/20')
# tag_data.set_key_value_pair(Key.year, '2021')
# picture_name = 'id3v2.3.jpg'
# with open('/home/thees/PycharmProjects/copy-audio-tag-to-another-audio-file/test/integration/fixtures/' + picture_name, "rb") as f:
#     picture_data = f.read()
# tag_data.picture = Picture(picture_name, picture_data)
# Mp3TagWriter(mp3_file_name).write(tag_data)

############################

# delete all tags from an mp3 file

# from mutagen.easyid3 import EasyID3
# mp3_file = EasyID3(mp3_file_name)
# mp3_file.delete()
# mp3_file.save()

############################

flac_file_name = '/home/thees/PycharmProjects/copy-audio-tag-to-another-audio-file/test/integration/fixtures/flac.flac'

flac_tag_fetcher = FlacTagFetcher(flac_file_name)
flac_tag_fetcher.fetch_tags()
flac_tag_fetcher.tag_data.pprint()
