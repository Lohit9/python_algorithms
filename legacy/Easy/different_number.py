'''
Question from Pramp:

Given an array arr of n unique non-negative integers, how can you most efficiently find a non-negative integer that is not in the array?

Your solution should return such an integer or null if arr contains all possible integers.
Analyze the runtime and space complexity of your solution.
'''

#Solution using a hash table
import sys

def diff_number(nums):
    if nums == []:
        return None
    d = dict()
    for each in nums:
        d[each] = 1
    for i in range(len(nums)):
        if i not in d:
            return i
    return len(nums)

print diff_number([4,5,2,1,0])
print diff_number([22,344,12,1,1,3,4,5])
print diff_number([0,1,2])
