import math


def root(x, n):
    return root_helper(x, n, 0, x)


def root_helper(x, n, start, end):
    guess = (start + end) / 2
    guess_pow = math.pow(guess, n)
    if abs(x - guess_pow) <= 0.001:
        return guess
    if guess_pow < x - 0.001:
        return root_helper(x, n, guess, end)
    else:
        return root_helper(x, n, start, guess)


print(root(2, 2))
print(root(8, 4))
