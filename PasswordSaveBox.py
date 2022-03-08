#!python3
passwords = {"email":"asdfasdfasdfasfdasdf",
"blog":"asdfasdfasdgdsfgsdfhdsghdrgfh",
"luggage":"asdfasdgsghfgnxbzvczsgjdrv"}
import sys, pyperclip
if len(sys.argv) < 2:
    print("Usage:python turtle.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]
if account in passwords:
    pyperclip.copy(passwords[account])
    print("password for " + account + " copied to clipboard")
else:
    print("there is no account named " + account)