#! python3
# PasswordLocker.py
import sys,pyperclip


import sys
if len(sys.argv) < 2:
    print('Usage: python PasswordLocker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] #first command line argument



PASSWORDS = {'email': 'KFADFSDFSDFASD',
             'blog,': 'gdfgdfgsdfgsdfg',
             'whatever': 'fasdfasdfasdf'}

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied.')
else:
    print('There is no acccount named' + account)

