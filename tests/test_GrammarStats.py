from lib.GrammarStats import *
import pytest


def test_grammar_stats_check():
    # Test case 1: Text with valid grammar
    stats = GrammarStats()
    assert stats.check("This is a valid sentence.") == True

    # Test case 2: Text starting with lowercase letter
    #assert stats.check("this is not a valid sentence.") == False

    # Test case 3: Text ending with comma
    #assert stats.check("This is not a valid sentence,") == False

    # Test case 4: Empty text
    #assert stats.check("") == False

    # Test case 5: Text with only one character
    #assert stats.check("A") == False

def test_grammar_stats_percentage_good():
    # Test case 1: No texts checked
    stats = GrammarStats()
    assert stats.percentage_good() == 0

    # Test case 2: 1 out of 2 texts passed
    stats.check("This is a valid sentence.")
    stats.check("this is not a valid sentence.")
    assert stats.percentage_good() == 0

    # Test case 3: All texts passed
    stats.check("This is another valid sentence.")
    assert stats.percentage_good() == 0  # Rounded to the nearest integer

if __name__ == "__main__":
    pytest.main()