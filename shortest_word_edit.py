def shortest_word_edit(source, target, words):
    if target not in words or len(source) != len(target):
        return -1

    diff = [(source, 0)]
    while diff:
        (source, count) = diff.pop(0)
        if source == target:
            return count

        diff.extend(compute_diff(source, count, words))


def compute_diff(source, count, words):
    diff = []
    for i in range(len(words)):
        one = 0
        for j in range(len(source)):
            if source[j] != words[i][j]:
                one += 1
        if one == 1:
            diff.append((words[i], count + 1))
    return diff


print(shortest_word_edit("bit", "dog", ["but", "put", "big", "pot", "pog", "dog", "lot"]))
