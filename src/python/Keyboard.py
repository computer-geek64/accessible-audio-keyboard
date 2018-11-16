#!/usr/bin/python3
# Keyboard.py
# Ashish D'Souza
# November 15th, 2018

import Autocomplete


class Layout:
    def __init__(self, width=7, height=6):
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.words = ["The", "I", "Yes", "No", "You", "Can", "Is"]
        self.width = width
        self.height = height
        self.keyboard = [
            ["The", "I", "Yes", "No", "You", "Can", "Is"],
            ["A", "B", "C", "D", "E", "F", "G"],
            ["H", "I", "J", "K", "L", "M", "N"],
            ["O", "P", "Q", "R", "S", "T", "U"],
            ["V", "W", "X", "Y", "Z", " ", ".,?!"],
            ["Backspace", "Clear", "Speak", "Shift", "0-9", "Del_Word", "Settings"]
        ]

    def set_alphabet(self, alphabet):
        for i in range(4):
            self.keyboard[i + 1] = alphabet[self.width * i:self.width * (i + 1)]

    def get_alphabet(self, text, shift=False):
        if text == "":
            return list(map(str.upper, self.alphabet)) + [" ", ".,?!"]
        else:
            predictions = Autocomplete.predict_character(text, max_suggestions=27)
            alphabet = predictions + [x for x in self.alphabet if x not in predictions]
            return alphabet if not shift else list(map(str.upper, alphabet)) + [".,?!"]

    def set_words(self, words):
        self.keyboard[0] = words

    def get_words(self, text, shift=False):
        if text == "":
            return list(map(str.capitalize, self.words))
        else:
            predictions = Autocomplete.predict_word(text, max_suggestions=7)
            return predictions if not shift else list(map(str.capitalize, predictions))
