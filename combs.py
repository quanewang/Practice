def combs(n):
    a = []
    if n == 0:
        return a
    for p in range(n + 1):
        for nic in range(int(n / 5) + 1):
            for d in range(int(n / 10) + 1):
                for q in range(int(n / 25) + 1):
                    if p + nic * 5 + d * 10 + q * 25 == n:
                        a.append([p, nic, d, q])
    return a

print(combs(100))


def recombs(n, a, choices):
    c = []
    if n == 0 or len(a) == 0:
        return c
    #acopy = a.copy()
    first = a.pop(0)
    for m in range(int(n / first) + 1):
        if n - m * first == 0:
            choices.append(m)
            c.append(choices)
            a.insert(0, first)
            # have to insert element back to maintain coin list integrity
            return c
        else:
            copy = choices.copy()
            copy.append(m)
            c.extend(recombs(n - m * first, a, copy))
    a.insert(0, first)
    return c

print(recombs(100, [1, 5, 10, 25], []))
a = combs(100)
b = recombs(100, [1, 5, 10, 25], [])

print(len(a) - len(b))
