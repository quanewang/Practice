def find_substring(s, words):
    indexes = []
    word_len = len(words[0])
    length = word_len * len(words)
    i = 0
    word_dict = {}

    for word in words:
        if word_dict.get(word) is None:
            word_dict.update({word: 1})
        else:
            word_dict.update({word: word_dict.get(word) + 1})

    while i + length - 1 < len(s):
        sub = s[i: i + length]
        if check_string(sub, word_dict.copy(), word_len):
            indexes.append(i)
        i += 1

    return indexes


def check_string(sub, dict_copy, word_len):
    i = 0
    while i < len(sub):
        str = sub[i: i + word_len]
        if dict_copy.get(str) is None or dict_copy.get(str) == 0:
            return False
        else:
            dict_copy.update({str: dict_copy.get(str) - 1})
        i += word_len
    return True






s = "barfoothefoobarman"
words = ["foo","bar"]
print(find_substring(s, words))

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(find_substring(s, words))

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(find_substring(s, words))

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print(find_substring(s, words))

s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]
print(find_substring(s, words))
