from lib.most_often import *

def test_initialise_list(): 
    starting_list = ["apple", "banana", "oranges", "apple"]
    most_often = MostOften(starting_list)
    assert most_often.starting_list == starting_list

def test_add_new():
    starting_list = ["apple", "banana", "oranges", "apple"]
    most_often = MostOften(starting_list) 
    most_often.add_new("oranges")
    assert most_often.starting_list == ["apple", "banana", "oranges", "apple", "oranges"]

def test_clear_winner():
    starting_list = ["apple", "banana", "oranges", "apple"]
    most_often = MostOften(starting_list) 
    result = most_often.get_most_often()
    assert result == "apple"

def test_no_clear_winner():
    starting_list = ["apple", "banana", "oranges", "apple", "oranges"]
    most_often = MostOften(starting_list) 
    result = most_often.get_most_often()
    assert result == "no clear winner"

def test_empty_list():
    starting_list = []
    most_often = MostOften(starting_list)
    result = most_often.get_most_often()
    assert result == "no clear winner"



