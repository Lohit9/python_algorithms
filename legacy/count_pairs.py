'''
Count the number of pairs in the list such that the difference is k
ex: [5 1 5 3 4 2]  => 3
ex: []
'''

'''
Idea:
bruteforce
'''

def pairs(nums, k):
    #a contains array of numbers and k is the value of difference
    count = 0
    for index, i in enumerate(nums):
        for j in nums[index+1:]:
            if abs(i - j) == k:
                count += 1
    return count

print pairs([1, 5, 3, 4, 2], 2)
