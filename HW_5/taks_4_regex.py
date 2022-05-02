import re
"""
Create separate regular expressions, which find the following patterns:
 Bulgarian National ID number (9-digit string, without any additional validity checks)
 An email
 A string, containing “hello”
"""



# AN EMAIL

# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#
# def check(email):
#     if (re.fullmatch(regex, email)):
#         print("Valid Email")
#
#     else:
#         print("Invalid Email")
#
# email = "ankitrai326@gmail.com"
# check(email)
#
# email = "my.ownsite@our-earth.org"
# check(email)
#
# email = "ankitrai326.com"
# check(email)

#===================================================================================================
# A string, containing “hello”
#
# txt = "The rain in Spain hello hello"
# x = re.findall("hello", txt)
# print(x)
#=================================================================================================

egn = '1234 12345 1234567 123456789 12345678910 1234567891011 egn qwertyuio qwertyuiop qwertyuiop[]asd'
zz = re.findall(' \d{9} ', egn)
print(zz)