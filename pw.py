#！ python3
# pw.py - An insecure password locker program.

PASSWORD = {'hotmail': 'why90230@hotmail.com',
            'hotmailp': 'hotmail password'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('Password for ' + account + 'copied to clipboard.')
else:
    print('There is no account named ' + account)