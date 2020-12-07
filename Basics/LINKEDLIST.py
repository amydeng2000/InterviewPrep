class Node:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

# Constructing a linked list
start = head = Node(0)
for i in range(1,5):
    head.next = Node(i)
    head = head.next


# REMOVE NODE
def delete(head, d): # remove node with data d, return the rest of the linked list
    # CHECK HEAD == NULL
    if not head: return head
    if head.val == d:
        return head.next
    ptr = head
    while ptr:
        # NEED THE POINTER BEFORE
        if ptr.next == d:
            ptr.next = ptr.next.next
            return head
        ptr = ptr.next
    return head


# APPROACH & TRICKS
"""
- Modify in-place or create an additional linked list?
- copying next data to the current node to delete the current node without having to access the previous pointer
- use hashmap to store nodes if we need to perform operations on the values
- runner technique
"""


# RUNNER TECHNIQUE
def interleave(head):
    """
    given an even length linkedlist, interleave the elements
    """
    if not head or not head.next: return head
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    fast = head
    while slow:
        temp = fast.next
        fast.next = slow
        fast = temp
        if not slow.next: # Important terminating condition!
            return head
        temp = slow.next
        slow.next = fast
        slow = temp
    return head


# REVERSE A LINKED LIST
def reverse(head):
    if not head: return head
    prev, curr = head, head.next
    while curr:
        temp = curr.next
        curr.next = prev
        prev, curr = curr, temp
    head.next = None  # REMEMBER TO SET FIRST NODE!
    return prev


res = reverse(start.next)
while res:
    print(res.val)
    res = res.next