"""
In this challenge, you will be given a string. You must remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Your goal is to create the longest string possible that contains just two alternating letters.
As an example, consider the string abaacdabd. If you delete the character a, you will be left with the string bcdbd. Now, removing the character c leaves you with a valid string bdbd having a length of 4. Removing either b or d at any point would not result in a valid string.
Given a string s, convert it to the longest possible string t made up only of alternating characters. Print the length of string t on a new line. If no string t can be formed, print 0 instead.

Function Description
Complete the alternate function in the editor below. It should return an integer that denotes the longest string that can be formed, or 0 if it cannot be done.
alternate has the following parameter(s):
s: a string

Input Format
The first line contains a single integer denoting the length of s. 
The second line contains string s.

Constraints
1 <= |s| <= 1000
s[i] in /a-z/

Output Format
Print a single integer denoting the maximum length of t for the given s; if it is not possible to form string t, print 0 instead.

Sample Input
beabeefeab

Sample Output
5

Explanation
t == babab -> len(t) == 5
"""
#!/bin/python3

import math
import os
import random
import re
import sys


def validate(s):#take a list not a tuple
    if len(s)>0:
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                return False
    return True

def sanitize(s):#take a list not a tuple
    again = True
    while again:
        l = set()
        for i in range(1,len(s)):
            if s[i] == s[i-1]: #remove s[i] letter
                l.add(s[i])
        if len(l) == 0:
            again = False
        for el in l:
            try:
                while True:
                    s.remove(el)
            except Exception: #ValueError: in python3.7, no specified in 3.5
                pass
# Complete the alternate function below.
def alternate(s):
    s = list(s)#change type since tuple is unmutable
    sanitize(s) # this function clean the string and delete all the unvalid possibility
    c = []
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[i] != s[j]:
            # create a list with 2 different chars
                arr = [c for c in s if c == s[i] or c == s[j]]
                if validate(arr):
                    c.append(arr)
    if len(c) == 0: return 0
    s = max(c,key=len)
    return len(s)
        

if __name__ == '__main__':
    print(alternate('beabeefeab'))