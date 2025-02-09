class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if not head or not head.next:
        return head

    # Find the middle of the list using slow and fast runner
    def findMiddle(node):
        slow, fast = node, node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Merge two sorted lists
    def merge(l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    # Recursive sort function
    middle = findMiddle(head)
    right_head = middle.next
    middle.next = None

    left_sorted = sortList(head)
    right_sorted = sortList(right_head)

    return merge(left_sorted, right_sorted)


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
values = [1, 2, 8, 4, 6, 5]
head = create_linked_list(values)
print_linked_list(head)
print_linked_list(sortList(head))

def insertionSortList(head):
    dummy = ListNode(0)  # Dummy node for the sorted part
    current = head

    while current:
        print_linked_list(current)
        prev = dummy
        # Find the correct position in the sorted part
        while prev.next and prev.next.val < current.val:
            prev = prev.next
        
        next_node = current.next  # Save next node to process
        # Insert current into the sorted part
        current.next = prev.next
        prev.next = current
        
        current = next_node  # Move to the next node

    return dummy.next

values = [1, 2, 8, 4, 6, 5]
head = create_linked_list(values)
print_linked_list(insertionSortList(head))

