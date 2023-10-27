#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str) or len(value) == 0:
            print("The value must be a string.")
        self.value = value
            
    def is_sentence(self):
        return self.value[-1] == "."
    
    def is_exclamation(self):
        return self.value[-1] == "!"
    
    def is_question(self):
        return self.value[-1] == "?"
    
    def count_sentences(self):
        if self.value and self.value != "The value must be a string.":
            value_list = self.value.replace(
                ".", "|"
            ).replace(
                "?", "|"
            ).replace(
                "!", "|"
            ).split("|")
            value_list = [list_str for list_str in value_list if len(list_str) > 0]
            return len(value_list)
        else:
            return 0