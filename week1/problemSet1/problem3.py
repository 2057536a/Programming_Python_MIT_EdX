#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 18:58:17 2018

@author: yannis
"""

#Write a program that prints the longest substring of s in which the letters 
#occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
#program should print

#"Longest substring in alphabetical order is: beggh"

#In the case of ties, print the first substring. For example, if s = 'abcbcd', 
#then your program should print

#"Longest substring in alphabetical order is: abc"



# Some test strings to check
#s = 'azcbobobegghakl'
#s = "abcbcd"
#s="ghhdozxovcdhllo"
#s = "zpodhtwtwnelsbwxvlthtgw"
s = "vhzgsvoyyfdaashtixfvxw"

# The initial string with an empty char in the end
# to avoid out of bounds exception. Will remove in the end
s += " "

#Make the first longest substring to be equals to the first char of the string at test
curr_longest_sub = s[0]


#Create a list to store the different alphabetically ordered substrings
# It will later be used for determining the longest one
subsList = []

#Iterate over the string
for i in range(len(s)):    
    #if the letter is after the last character of the current 
    # longest substring
    if (s[i] >= curr_longest_sub[-1]):
        #, then add it to the current longest
        curr_longest_sub += s[i]
    # if not    
    else:
        #then add the existing longest substring
        ## to the substrings list for comparing later
        subsList.append(curr_longest_sub)
        #reset the current substring 
        curr_longest_sub = s[i]

#Remove the extra space from the first array element
subsList[0] = subsList[0][1:]

#Now determine which substring in the list has the greatest length
# Lets set the first entry as the longest so far
max_len = len(subsList[0])
max_sub = subsList[0]


# iterate over the list elements and if you find
# an element longer than the current longest one,
# make it the new longest
for elem in subsList:
    if len(elem)>max_len:
        max_sub = elem
        max_len = len(elem)

#Print final result of the longest substring
print("Longest substring in alphabetical order is: " + max_sub)


        