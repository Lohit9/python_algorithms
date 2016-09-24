"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
# runtime complexity is O(n^2)
def two_sum_2(nums,target):
    for index in range(len(nums)):
        rem = target - nums[index]
        for index2 in range(index+1, len(nums)):
          if rem == nums[index2]:
             print index, index2
             return;

#runtime complexity is O(n^2) because list.index(elem) searches the list and hence has an O(n) complexity
def two_sum3(nums,target):
    for each in nums:
        subarr = nums[(nums.index(each)+1):len(nums)]
        rem = target - each
        if rem in subarr:
          act_index = subarr.index(rem) + (len(nums) - len(subarr))
          print nums.index(each), act_index
          return;


two_sum([3,2,4], 6) #[1,2]
two_sum([2,7,11,15], 9) #[0,1]
two_sum([0,4,3,0], 0) #[0,0]
