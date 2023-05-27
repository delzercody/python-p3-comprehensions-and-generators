#!/usr/bin/env python3

def return_evens(num_list):
    even_num_list = [num for num in num_list if num % 2 == 0]

    return even_num_list

def make_exclamation(sentence_list):
    new_sentence_list = [sentence + "!" for sentence in sentence_list]
    return new_sentence_list