#!/usr/bin/env python3

def is_palindrome(check):
    """Take a string and return whether or not it's a palindrome."""

    # Strip special characters and capitalize entire string
    caps = ''.join(i for i in check if i.isalnum()).upper()

    # Check each character against its match on the other end of the string
    for char in range(len(caps) // 2):
        if caps[char] != caps[-(char+1)]:
            return False
    return True

check = input('Type word to check: ')

print('\'' + check + '\' is' + (' ' if is_palindrome(check) else ' not ') + 'a palindrome.')
