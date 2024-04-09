## 1. Describe the Problem

# > As a user 
# > So that I can keep track of my phone numbers
# > I want to keep a record of all phone numbers I use in my diary entries

# * We may want to look thru multiple diary entries
# * Phone numbers are 11-digit numbers, starting with zero
import re
class PhoneBook():
    
    def __init__(self):
        self._numbers = []
    
    def extract_numbers(self, diary_entry):
        numbers = re.findall(r'[0-9]+', diary_entry)
        self._numbers += numbers

    def list_numbers(self):
        return self._numbers