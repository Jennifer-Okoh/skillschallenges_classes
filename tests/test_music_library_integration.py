from lib.music_library import MusicLibrary
from lib.track import Track

#def test_music_library_integration():
"""
Given I add two tracks
I can see them represented in the list
"""
def test_adds_multiple_tracks_and_list_and_list_them():
    library = MusicLibrary()
    track_1 = Track("My Title 1", "My Artist 1")
    track_2 = Track("My Title 2", "My Artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library.all() == [track_1, track_2]

"""
Initially
There are no tracks
"""
def test_initially_has_no_tracks():
    library = MusicLibrary()
    assert library.all() == []

"""
Given I add two tracks
If I search for the title of one of the tracks
I get that track back in the results
"""
def test_search_by_title():
    library = MusicLibrary()
    track_1 = Track("My Title 1", "My Artist 1")
    track_2 = Track("My Title 2", "My Artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("My Title 2") == [track_2]

"""
Given I add two tracks
If I serach for part of the title of one of the tracks
I get the matching track back in the results
"""

def test_searches_by_part_of_title():
    library = MusicLibrary()
    track_1 = Track("My Title 1", "My Artist 2")
    track_2 = Track("My Title 3", "My Artist 4")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("1") == [track_1]