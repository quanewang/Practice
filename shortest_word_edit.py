# breadth-first search problem
def shortest_word_edit(source, target, words):
    if target not in words or len(source) != len(target):
        return -1

    diff = [(source, 0)]
    used = [source]
    while diff:
        (source, count) = diff.pop(0)
        if source == target:
            return count

        diff.extend(compute_diff(source, count, words, used))

    return -1


def compute_diff(source, count, words, used):
    diff = []
    for i in range(len(words)):
        one = 0
        if words[i] not in used:
            for j in range(len(source)):
                if source[j] != words[i][j]:
                    one += 1
            if one == 1:
                diff.append((words[i], count + 1))
                used.append(words[i])
    return diff


print(shortest_word_edit("bit", "dog", ["but", "put", "big", "pot", "pog", "dog", "lot"]))
print(shortest_word_edit("no", "go", ["to"]))
