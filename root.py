import math


def root(x, n):
    return root_helper(x, n, x / 2, x / 2, x)


def root_helper(x, n, guess, start, end):
    guess_pow = math.pow(guess, n)
    if abs(x - guess_pow) <= 0.001:
        return guess
    increment = (end - guess) / 2
    if guess_pow < x - 0.001:
        return root_helper(x, n, guess + increment, guess, end)
    else:
        return root_helper(x, n, guess - increment, start, guess)


print(root(2, 2))