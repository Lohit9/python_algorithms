'''
Given 2 sorted arrays find the median of the two sorted arrays.

[1,2,3]


Idea:
how would you convert an array into a bst?
'''
class Node(object):
    def __init__(val, left = None, right= None):
        Node.val = val
        Node.left = left
        Node.right = right
#assumng global def of Node

# # [1,2,3,4,5,6] => 4          [1,2,3,4,5]  => [1,2]  3 [4,5]
# #                 / \         [1,2] =>1 2
# #                3   5
# #               /     \
# #              2       6
#               /
#              1
def medianIndex(start, end):
        l = start + end + 1
        index = 0
        if(l%2 is not 0):
            index = (l+1)/2 - 1
        else:
            index = l/2 + 1
        return index

def sortedArrayToBst(nums):
    medianIndex = findMedianIndex(nums)
    bstNode->val = nums[medianIndex]
    bstNode->left = sortedArrayToBst(nums[:medianIndex])
    bstNode->right = sortedArrayToBst(nums[medianIndex:])
    bstNode->centrer   sortedArrayToBst
# Idea: given an array how to build a bst out of it?

def build_bst(nums):
