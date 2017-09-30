# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
# non-zero elements.
#
# For example,
# given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#

def moveZeroes(nums):
    count = nums.count(0)
    while 0 in nums:
        nums.remove(0)
    for i in range(count):
        nums.append(0)

moveZeroes([0, 1, 0, 3, 12])
