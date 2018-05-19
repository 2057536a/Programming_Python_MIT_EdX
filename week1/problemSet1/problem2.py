#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 16:05:47 2018

@author: yannis
"""

#Assume s is a string of lower case characters.
#Write a program that prints the number of times 
#the string 'bob' occurs in s. For example, 
#if s = 'azcbobobegghakl', then your program should 
#print
#
#        Number of times bob occurs is: 2


#Test string decleration
s = 'azcbobobegghakl'

# Elongate the test string by 2 
# empty characters (since the substring
# we need to check against has 2 chars after the first one)
s += '  '

# Substring declaration and variable to hold the 
# occurence in the tested string
sub = 'bob'
count = 0

#Iterate over the string. For each char, if the char is 'b', and 
# the next one is 'o' and the the next after that is 'b' then 
#we have an occurence of the substring. IN that case increment the count
for i  in range(len(s)-2):
    if (s[i] + s[i+1]+ s[i+2]) == sub:
        count += 1

#Print the result
print("Number of times bob occurs is: " + str(count))        