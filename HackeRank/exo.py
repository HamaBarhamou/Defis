#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'buildPalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def sous_chaine(ch):
    s=[]

    for i in range(len(ch)):
        for j in range(i+1, len(ch)+1, 1):
            s.append(''.join(ch[i:j]))
    return s

def buildPalindrome(a, b):
    # Write your code here
    s_a = sous_chaine(a)
    s_b = sous_chaine(b)
    
    pali=[]
    
    for i in range(len(s_a)):
        for j in range(len(s_b)):
            ch = s_a[i] + s_b[j]
            if ch == ch[::-1]:
                pali.append(ch)
                #print(ch)
                
    for i in range(len(s_b)):
        for j in range(len(s_a)):
            ch = s_b[i] + s_a[j]
            if ch == ch[::-1]:
                pali.append(ch)
                #print(ch)
 
    pali.sort()
    
    if len(pali) != 0:
        return max(pali, key=len)
    else:
        return "-1"
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        result = buildPalindrome(a, b)

        fptr.write(result + '\n')

    fptr.close()
