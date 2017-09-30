# //Reverse a linked list

// 2 --> 4 --> 5 --> 6

def revllist(node):
    if not node: return None
    elemList = []
    while(node.next not None):
        elemList.append(node)
        node = node.next
    node = None
    for each in elemList.reverse():
        node = each
        node.next = None
        node = node.next

    return node
