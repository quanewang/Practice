def flatten_dictionary(dictionary):
    return flatten_helper(dictionary)


def flatten_helper(dictionary, parent_key=""):
    flattened_dict = {}

    for key in dictionary.keys():
        x = dictionary.get(key)
        if parent_key != "":
            key = parent_key + "." + str(key)
        if type(x) == dict:
            flattened_dict.update(flatten_helper(x, key))
        else:
            flattened_dict.update({key: x})
    return flattened_dict


dictionary = {
    "Key1": "1",
    "Key2": {
        "a": "2",
        "b": "3",
        "c": {
            "d": "3",
            "e": {
                "": "1"
            }
        }
    }
}

print(flatten_dictionary(dictionary))

