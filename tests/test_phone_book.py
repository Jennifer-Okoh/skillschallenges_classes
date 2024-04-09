from lib.phone_book import *

def test_initially_has_no_numbers():
    phone_book = PhoneBook()
    assert phone_book.list_numbers() == []

def test_extracts_numbers_from_a_single_entry():
    phone_book = PhoneBook()
    phone_book.extract_numbers("My husband's number is 0770000000")
    assert phone_book.list_numbers() == ["0770000000"]

def test_extracts_numbers_from_multiple_entries():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Eric's number is 0770000001")
    phone_book.extract_numbers("Sarah's number is 0770000002")
    phone_book.extract_numbers("Joe's number is 0770000003")
    assert phone_book.list_numbers() == ["0770000001", "0770000002", "0770000003"]

    

