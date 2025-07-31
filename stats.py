def count_words(string):
    num_words = len(string.split())
    return num_words

def count_chars(string):
    chars_dictionary = dict()
    for char in string.lower():
        if char not in chars_dictionary:
            chars_dictionary[char] = 0
        chars_dictionary[char] += 1
    return chars_dictionary

def sort_dictionary(dict):
    sorted_list = list()
    for value in dict:
        sorted_list.append(value["char"])
    print(sorted_list)

