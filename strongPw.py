#！ python3
# strongPw.py - Check whether the input password is strong(contain Upper, Lower and number).

import re

# Get the input
pw = input("Type in your password:")
result = False

# Upper, Lower and number regex
upperRegex = re.compile('[A-Z]')
lowerRegex = re.compile('[a-z]')
numRegex = re.compile('[0-9]')

# Check the input
mo_upper = upperRegex.search(pw)
mo_lower = lowerRegex.search(pw)
mo_num = numRegex.search(pw)
result = (len(pw) > 8) and mo_num and mo_lower and mo_upper

# Print the infomation
if result:
    print('Your password is good.')
else:
    print('Your password must contain Upper, Lower and number, besides longer than 8 characters.')