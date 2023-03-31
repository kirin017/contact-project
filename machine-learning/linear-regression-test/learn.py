#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hh = s[:2]
    ms = s[2:8]
    APdate = s[8:]
    if APdate == 'AM':
        if int(hh) >= 12:
            h = int(hh)-12
        
    if APdate == 'PM':
        if int(hh) < 12:
            h=int(hh)+12        
    date =str(h)+ms
    elif h < 10:
        date = '0'+date
    return date

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result + '\n')
    #fptr.write(result + '\n')

    #fptr.close()
