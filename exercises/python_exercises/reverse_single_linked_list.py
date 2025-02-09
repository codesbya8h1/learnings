from typing import Optional

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def linked_list_reversal(head: Optional[ListNode]) -> Optional[ListNode]:
    # Initialize pointers
    prev = None
    current = head
    

    # Traverse and reverse links
    while current:
        # Print debug information for clarity
        print(f"Current Node Value: {current.val if current else 'None'}")
        print(f"Prev Node Value: {prev.val if prev else 'None'}")
        
        # Save next node
        next_node = current.next
        
        # Reverse link
        current.next = prev
        
        # Move pointers forward
        prev, current = current, next_node
    
    # Return new head (prev)

    return prev

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

reversed_head = linked_list_reversal(head)
print("Reversed Linked List:")
print_linked_list(reversed_head)
