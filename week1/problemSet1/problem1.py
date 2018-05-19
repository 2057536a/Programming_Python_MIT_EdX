#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 16:01:02 2018

@author: yannis
"""

#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels 
#contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
#For example, if s = 'azcbobobegghakl', your program should print:
#
#                    Number of vowels: 5



#Test string declaration
s = 'azcbobobegghakl'

# Variable to hold the number of vowels in a string
count = 0

# Iterate over the string elements to check if they
# correspond to a vowel value
for e in s:
    if e == "a" or e == "e" or e == "i" or e == "o" or e =="u":
        count += 1
        
print("Number of vowels: " + str(count))
        
