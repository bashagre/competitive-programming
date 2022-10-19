#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    output = []
    for o in range(len(grades)):
        if grades[o] < 38:
            output.append(grades[o])
        
        elif grades[o] >= 38: 
            for i in range(3):
                if (grades[o]+i) % 5 == 0:
                    output.append(grades[o]+i)
                    break
            else:
                output.append(grades[o])
    return output
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
