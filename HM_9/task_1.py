"""
Write a function that uses regular expressions to make sure the password string it is passed is strong.
A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.
"""

import re

strong_pass = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$')

# passcheck = strong_pass.match("123")
# passcheck = strong_pass.match("Cveti")
# passcheck = strong_pass.match("Cveti12")
# passcheck = strong_pass.match("Testing193!")
# passcheck = strong_pass.match("Cveti67")
# passcheck = strong_pass.match("cveti678")
# passcheck = strong_pass.match("cvetiasdasdasdasd")
# passcheck = strong_pass.match("Cvetiasdasdasdasd")
passcheck = strong_pass.match("Cveti678")
print(passcheck)
