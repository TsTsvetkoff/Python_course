"""
Create a function has_vowel, that accepts a string and returns True
if the string contains a vowel (a, e, i, o, or u) returns False otherwise.
"""

import re

my_validator = re.compile(r'[aeiou]')
# check_string = my_validator.search("nnnn")
# check_string = my_validator.search("qwrtypsdfghjklzxcvbnm")
# check_string = my_validator.search("aeiou")
# check_string = my_validator.search("Bira")
check_string = my_validator.search("Vino")


def has_vowel(check_string):
    match_requriemtn = False
    if 'match' in str(check_string):
        match_requriemtn = True
        print(match_requriemtn)
    else:
        print(match_requriemtn)


has_vowel(check_string)
