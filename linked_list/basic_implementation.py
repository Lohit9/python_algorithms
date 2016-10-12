#  This file contains the implementation of a linked list node and contains a set of basic operation that can be done:
#    * Insertion
#    * Deletion
#    * Printing
#    * Finding an element

class Node(object):
    def __init__(self, data = None, next_node = None) :
        self.data = data
        self.next_node = next_node

    def print_list(self):
        if not list:
            print 'NULL'
            return
        while self.next_node != None:
