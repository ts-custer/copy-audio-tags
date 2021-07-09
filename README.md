# copy-audio-tags

Python script that copies audio tag information of an audio file to another audio file

2021-06-24: At the moment only .mp3 and .flac files are supported.

Requires https://github.com/ts-custer/mutagen-wrapper

```
usage: __main__.py [-h] [-t] [-u] [-r OLD NEW] source_directory

positional arguments:
  source_directory      Directory with audio files to copy audio tags from

optional arguments:
  -h, --help            show this help message and exit
  -t, --test_mode       If you set option -t ('test'), nothing will be saved
  -u, --update_comment  If you set option -u ('update comment'), the 'comment'
                        tag field will get the current date
  -r OLD NEW, --replace OLD NEW
                        To specify a textual replacement in the to be copied
                        tags
```
