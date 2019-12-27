from contextlib import contextmanager
from collections import OrderedDict
import xml.etree.cElementTree as ET


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
    return ordered_dict


def convert_dict_to_xml(resource_dict, xml_file_name):
    root = ET.Element('root')
    word = ET.SubElement(root, 'word')
    field_counter = 0
    for key, val in resource_dict.items():
        field_counter += 1
        ET.SubElement(word, ('field'+str(field_counter)), name=key).text = str(val)

    tree = ET.ElementTree(root)
    xml_output_file = tree.write(xml_file_name, xml_declaration=True, encoding='utf-8')
    return xml_output_file


def transdorm_text_to_xml(text_file_name, xml_file_name):
    with open_file(text_file_name, 'r') as resource:
        file_content = resource.read()
        resource.close()

    words_from_file = get_dict_of_words_from_string(file_content)
    ordered_dict_words = order_dict_by_value(words_from_file)
    convert_dict_to_xml(ordered_dict_words, xml_file_name)


transdorm_text_to_xml('rur.txt', 'rur.xml')

with open_file('rur.xml', 'r') as resource:
    file_content = resource.read()
    resource.close()