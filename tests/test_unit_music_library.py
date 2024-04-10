from lib.music_library import MusicLibrary

# def test_music_library():
#     library = MusicLibrary()

#   # ...

"""
Initially
There are no tracks
"""
def test_initially_has_no_tracks():
    library = MusicLibrary()
    assert library.all() == []

"""
Initially
Seraching for tracks get an empty list
"""

def test_initially_gets_empty_list():
    library = MusicLibrary()
    assert library.search_by_title("hello") == []