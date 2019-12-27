from contextlib import contextmanager
from collections import OrderedDict


@contextmanager
def open_file(file_name, mode):
    file = open(file_name, mode)
    yield file
    file.close()

def get_dict_of_words_from_string(resource_string):
    all_words = {}

    # divide into lines - tuple with strings - lines
    raw_lines = resource_string.split('\n')

    list_of_characters_to_strip = [' ', '"', '“', '„', '\'', ',', ';', '…', '.', '?', '!', ':', '-', '–']

    # go through lines in tuple
    for line in raw_lines:
        # divide each line from tuple into words (raw_words_from_line = tuple with words)
        raw_words_from_line = line.split(' ')
        for raw_word in raw_words_from_line:
            word = raw_word.lower()
            # strip the characters from the list
            for i in list_of_characters_to_strip:
                word = word.strip(i)

            if word == '':
                continue

            if word in all_words:
                all_words[word] += 1
            else:
                all_words[word] = 1
    return all_words


def order_dict_by_value(resource_dict):
    ordered_dict = OrderedDict(sorted(resource_dict.items(), key=lambda x: x[1], reverse=True))
    print(ordered_dict)
    # list of keys
    ordered_dict_keys = ordered_dict.keys()
    for item in ordered_dict_keys:
        print(item, ordered_dict[item])

with open_file('rur.txt', 'r') as resource:
    file_content = resource.read()

words_from_file = get_dict_of_words_from_string(file_content)
print(words_from_file)

ordered_words_from_file = order_dict_by_value(words_from_file)


