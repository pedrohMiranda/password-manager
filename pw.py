#! /usr/bin/python3

# pw.py - Password Manager

Passwords = {
  'email': 'name@email.com',
  'blog': 'blog.com',
  'luggage': '1234'
}

import sys, pyperclip

if len(sys.argv) < 2:
  print('Usage: ./pw.py [account] - copy account password')
  sys.exit()

account = sys.argv[1]

if account in Passwords:
  pyperclip.copy(Passwords[account])
  print('Password for ' + account + 'copied to clipboard.')
else:
  print('There is no account named ' + account)
