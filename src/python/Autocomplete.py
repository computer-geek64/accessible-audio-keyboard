#!/usr/bin/python3
# Autocomplete.py
# Ashish D'Souza
# November 15th, 2018

import autocomplete


autocomplete.load()


def predict_character(text, max_suggestions=27):
    if " " not in text:
        results = autocomplete.predict_currword(text.lower(), top_n=max_suggestions)
        characters = [x[0][len(text)] if not x[0][len(text):] == "" else " " for x in results]
    else:
        words = text.lower().split(" ")
        results = autocomplete.predict_currword_given_lastword(words[-2], words[-1], top_n=max_suggestions)
        characters = [x[0][len(words[-1])] if not x[0][len(words[-1]):] == "" else " " for x in results]
    probabilities = [x[1] for x in results]
    character_dict = {}
    for character in range(len(characters)):
        character_dict[characters[character]] = sum([probabilities[x] for x in range(len(characters)) if characters[character] == characters[x]])
    return sorted(character_dict, key=character_dict.__getitem__, reverse=True)


def predict_word(text, max_suggestions=10):
    if " " not in text:
        results = [x[0] for x in autocomplete.predict_currword(text.lower(), top_n=max_suggestions)]
    else:
        words = text.lower().split(" ")
        results = [x[0] for x in autocomplete.predict_currword_given_lastword(words[-2], words[-1], top_n=max_suggestions)]
    return results
