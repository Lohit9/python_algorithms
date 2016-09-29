'''
Todo: complexity can be cut down to linear, current: O(nlogn)
'''

# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the
# very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].

#idea: first find all the windows and then find the maximum in each window
import unittest

def sliding_window(nums, k):
    result = []
    for i in range(len(nums)):
        subarr = nums[i:]
        window = subarr[0:k]
        if len(window) == k:
            window.sort()
            result.append(window[-1])
    return result

class TestCases(unittest.TestCase):
    def test_example_test(self):
        self.assertEqual(sliding_window([], 0), [])
        self.assertEqual(sliding_window([2], 1), [2])
        self.assertEqual(sliding_window([1,3,-1,-3,5,3,6,7], 3), [3, 3, 5, 5, 6, 7])

if __name__ == '__main__' :
    unittest.main()
