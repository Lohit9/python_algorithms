# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array nums = [1,1,2],

def removeDuplicates(nums):
    if (len(nums) == 1): return nums
    for i in xrange(len(nums)):
        while(i < len(nums)-1 and nums[i] == nums[i+1]):
            nums.pop(i)
    return nums


print removeDuplicates([1,1,1,1,1,1])
print removeDuplicates([1])
print removeDuplicates([])
print removeDuplicates([1,1,1,2,2,2])
