def combs(n):
    a = []
    if n == 0:
        return a
    for p in range(n + 1):
        for nic in range(n // 5 + 1):
            for d in range(n // 10 + 1):
                for q in range(n // 25 + 1):
                    if p + nic * 5 + d * 10 + q * 25 == n:
                        a.append([p, nic, d, q])
    return a

print(combs(100))


def recombs(n, a, choices):
    c = []
    if n == 0 and len(a) == 0:
        return [choices]
    if len(a) == 0 and n != 0:
        return c
    #acopy = a.copy()
    first = a.pop(0)
    for m in range(n // first + 1):
        copy = choices.copy()
        copy.append(m)
        c.extend(recombs(n - m * first, a, copy))
    a.insert(0, first)
    return c

print(recombs(100, [1, 5, 10, 25], []))
a = combs(100)
b = recombs(100, [1, 5, 10, 25], [])

print(len(a) - len(b))
