"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
'''
idea:

if empty return false
create a hash table between the data and freq of occurence and return if > 1
'''

def hasCycle(self, head):
        if not head: return False
        nodesList = []
        while(head):
           if head in nodesList:
               return True
           else:
               nodesList.append(head)
           head = head.next
        return False

def hasCycle(self, head):
    fast = head
    slow = head
    while(fast.next && fast.next.next):
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False
