"""
Linked List Loop
Easy
Given a singly linked list, determine if it contains a cycle. A cycle occurs if a node's next pointer references an earlier node in the linked list, causing a loop.

Example:


Output: True
"""

from typing import Optional

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    # Write your code here
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Example usage
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)
print("Original Linked List:")
print_linked_list(head)

# Example Usage
# Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> back to node 3
head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = third  # Creates a cycle

print(hasCycle(head))  # Output: True

# Create a linked list without a cycle: 1 -> 2 -> 3 -> None
head2 = ListNode(1)
second2 = ListNode(2)
third2 = ListNode(3)

head2.next = second2
second2.next = third2

# print(hasCycle(head2)) 