from lib.age_checker import *
import pytest


def test_for_valid_age():
    result = age_checker("2003-07-21")
    assert result == "Access Granted"

def test_for_underage():
    result = age_checker("2010-07-22")
    assert result == "You are too young, you are 13. You need to be 16"

def test_wrong_format():
    with pytest.raises(Exception) as e:
        result = age_checker("07-07-07")
    error_message = str(e.value)
    assert error_message == "Incorrect date format"
    


    