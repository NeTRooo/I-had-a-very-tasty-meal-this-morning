#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def count_vowels(input_string):
    vowels = set("aeiouAEIOU")
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

if __name__ == "__main__":
    input_string = input("Введите строку: ")

    result = count_vowels(input_string)
    print("Количество гласных в строке:", result)
