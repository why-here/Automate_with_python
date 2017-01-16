#! python
# strip_Regex.py - Implement the strip function with regex.

import re

def strip_Regex(str_para, sub_str = None):
    # Strip space in the begin and the end of string
    if sub_str is None:
        spaceRegex = re.compile(r'(^\s*)?(\s*$)?')
        result = spaceRegex.sub('', str_para)
    # Strip sub_str in the string
    else:
        strRegex = re.compile(sub_str)
        result = strRegex.sub('', str_para)
    return result

# Get the string 
string = input('String:')
sub_str = input('String to strip:')
sub_str = None if len(sub_str)==0 else sub_str
print('Result:\n')
print(strip_Regex(string, sub_str))
