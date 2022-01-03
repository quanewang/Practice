import re


def word_count_engine(document):
    word_dict = {}
    copy = document.replace('.', '')
    copy = copy.replace('?', '')
    copy = copy.replace('!', '')
    copy = copy.lower()
    list_of_words = re.split('; | |,', copy)
    max_occurrence = 1
    for i in range(len(list_of_words)):
        string = list_of_words[i].replace("'", '')
        list_of_words[i] = string
        values = word_dict.get(string)
        if values is None:
            word_dict.update({string: (1, i)})
        else:
            newValues = (values[0] + 1, values[1])
            if max_occurrence < values[0] + 1:
                max_occurrence = values[0] + 1
            word_dict.update({string: newValues})

    occurrence_dict = {}
    for i in range(len(list_of_words)):
        string = list_of_words[i]
        occurrence = word_dict.get(string)[0]
        if occurrence_dict.get(occurrence) is None:
            occurrence_dict.update({occurrence: [string]})
        else:
            list_strings = occurrence_dict.get(occurrence)
            if i == word_dict.get(string)[1]:
                list_strings.append(string)
                occurrence_dict.update({occurrence: list_strings})
    output = []
    for i in range(max_occurrence, 0, -1):
        strings = occurrence_dict.get(i)
        for j in range(len(strings)):
            output.append([strings[j], str(i)])

    return output


file = "Practice makes perfect. you'll only get? Perfect by practice. just practice!"

print(word_count_engine(file))
