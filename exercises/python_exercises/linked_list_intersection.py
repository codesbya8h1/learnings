class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def linked_list_intersection(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    # Initialize two pointers
    a, b = headA, headB

    # Traverse both lists
    while a != b:
        # Move to next node or switch to the other list's head
        a = a.next if a else headB
        b = b.next if b else headA

    # Either they meet at an intersection node or both become null (no intersection)
    return a

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

# Helper function to print a linked list from a given node
def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

# Example Usage
# Create two intersecting linked lists:
# List A: 1 -> 2 -> 3 \
#                       -> 8 -> 9
# List B:       4 -> 5 /
common = create_linked_list([8, 9])
headA = create_linked_list([1, 2, 3])
headB = create_linked_list([4, 5])

# Attach common part to both lists
tailA = headA
while tailA.next:
    tailA = tailA.next
tailA.next = common

tailB = headB
while tailB.next:
    tailB = tailB.next
tailB.next = common

print("List A:")
print_linked_list(headA)

print("List B:")
print_linked_list(headB)

# Find intersection
intersection_node = linked_list_intersection(headA, headB)
if intersection_node:
    print(f"Intersection Node: {intersection_node.val}")
else:
    print("No Intersection")