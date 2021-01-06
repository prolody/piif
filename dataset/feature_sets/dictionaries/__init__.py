"""
dictionary wordlists
"""


import os

from .. import word_list_counter

NAME = 'dictionary'

raw_dict_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'raw',
    'NL-dictionary-file',
    'dutch.dic'
)

raw_pop_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'raw',
    'top1000.txt'
)

def get_wordlists(line_printer_cb):
    word_list =     word_list_counter.WordListCounter()
    word_list_pop = word_list_counter.WordListCounter()
    with open(raw_dict_path) as dict_file:
        dict_words = dict_file.readlines()
        for word in dict_words:
            words = word.split(' ') # ?
            for w in words:
                word_list.check_and_add(w)
            line_printer_cb('main: {}'.format(word_list.count))

    # new line
    line_printer_cb(None)

    with open(raw_pop_path) as dict_file:
        dict_words = dict_file.readlines()
        for word in dict_words:
            words = word.split(' ') # ?
            for w in words:
                word_list_pop.check_and_add(w)
            line_printer_cb('pop: {}'.format(word_list_pop.count))

    return {'main': word_list.keys, 'pop': word_list_pop.keys}