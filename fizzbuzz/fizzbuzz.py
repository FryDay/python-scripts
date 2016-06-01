#!/usr/bin/env python3

def get_input():
    low = input('Enter low end of range: ')
    high = input('Enter high end of range: ')
    try:
        low = int(low)
        high = int(high)
        assert high > low
    except(ValueError, AssertionError):
        print('Invalid range')
        return get_input()

    return (low, high)

user_range = get_input()

for num in range(user_range[0], user_range[1] + 1):
    txt = ''
    if num % 3 == 0:
        txt += 'Fizz'
    if num % 5 == 0:
        txt += 'Buzz'

    print(txt or num)
