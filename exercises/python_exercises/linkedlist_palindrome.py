class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True  # A single node or empty list is always a palindrome

    # Step 1: Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # Step 3: Compare both halves
    left, right = head, prev  # 'left' starts from head, 'right' starts from reversed second half
    while right:  # Only need to compare till 'right' ends
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    # Optional Step 4: Restore the original list (not required unless explicitly stated)
    # Reverse the second half again to restore original structure

    return True

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

# Example Usage
values1 = [1, 2, 2, 1]
head1 = create_linked_list(values1)
print(is_palindrome(head1))  # Output: True

values2 = [1, 2, 3]
head2 = create_linked_list(values2)
print(is_palindrome(head2))  # Output: False
