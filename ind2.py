#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    set_of_chars1 = set(string1)
    set_of_chars2 = set(string2)

    common_chars = set_of_chars1.intersection(set_of_chars2)

    if common_chars:
        print("Common characters:", common_chars)
    else:
        print("No common characters.")