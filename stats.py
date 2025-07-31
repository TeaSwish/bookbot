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

def sort_by(dict):
    return dict["count"]

def sort_dictionary(dict):
    sorted_list = []
    for k, v in dict.items():
        new_dict = {"char": k, "count": v}
        sorted_list.append(new_dict)
    sorted_list.sort(key=sort_by, reverse=True)
    return sorted_list
    # Sort by value in descending order
