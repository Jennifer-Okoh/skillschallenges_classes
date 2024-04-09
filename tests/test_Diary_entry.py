
from lib.Diary_entry import *

def test_format_entry_with_title_and_contents():
    diary_entry = DiaryEntry("My title", "Some contents")
    result = diary_entry.format()
    assert result == "My title: Some contents"

def test_count_number_of_words_in_diary():
    diary_entry = DiaryEntry("My title", "Some contents")
    result = diary_entry.count_words()
    assert result == 4

def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntry("My title", "one two")
    result = diary_entry.reading_time(2)
    assert result == 1

def test_reading_time_with_two_wpm_and_three_words():
    diary_entry = DiaryEntry("My title", "one two three")
    result = diary_entry.reading_time(2)
    assert result == 2

def test_reading_time_with_two_wpm_and_four_words():
    diary_entry = DiaryEntry("My title", "one two three four")
    result = diary_entry.reading_time(2)
    assert result == 2

import pytest


# def test_diary_entry_format():
#     # Test case 1: Format with title and contents
#     entry = DiaryEntry("My Title", "These are the contents")
#     assert entry.format() == "My Title: These are the contents"

# def test_diary_entry_count_words():
#     # Test case 1: Count words in contents
#     entry = DiaryEntry("My Title", "These are the contents")
#     assert entry.count_words() == 4

# def test_diary_entry_reading_time():
#     # Test case 1: Calculate reading time
#     entry = DiaryEntry("My Title", "These are the contents")
#     assert entry.reading_time(200) == 1  # Assuming 200 words per minute

# def test_diary_entry_reading_chunk():
#     # Test case 1: Reading chunk with 1 minute
#     entry = DiaryEntry("My Title", "These are the contents")
#     assert entry.reading_chunk(200, 1) == "These are the contents"

#     # Test case 2: Reading chunk with 0 minutes (empty chunk)
#     assert entry.reading_chunk(200, 0) == ""

#     # Test case 3: Reading chunk with multiple minutes
#     assert entry.reading_chunk(200, 2) == "These are the"
#     assert entry.reading_chunk(200, 2) == "contents"
#     assert entry.reading_chunk(200, 2) == ""  # End of contents

#     # Test case 4: Reading chunk with 0 wpm (empty chunk)
#     assert entry.reading_chunk(0, 1) == ""

#     # Test case 5: Restart reading from the beginning
#     assert entry.reading_chunk(200, 2) == "These are the"
#     assert entry.reading_chunk(200, 2) == "contents"
#     assert entry.reading_chunk(200, 2) == ""  # End of contents
#     assert entry.reading_chunk(200, 2) == "These are the"  # Restart from beginning

# if __name__ == "__main__":
#     pytest.main()