# Remove the Kth Last Node From a Linked List

# Return the head of a singly linked list after removing the kth node from the end of it.

# Constraints:
# The linked list contains at least one node.


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def remove_kth_list_node(head: ListNode, k: int) -> ListNode:
    # Write your code here
    
    # Create a dummy node to simplify edge cases (e.g., removing head)
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Step 1: Move `first` pointer k+1 steps ahead
    for _ in range(k + 1):
        if not first:  # If k is greater than the length of the list
            return head
        first = first.next

    # Step 2: Move both pointers until `first` reaches the end
    while first:
        print("first :", first.val)
        
        first = first.next
        second = second.next
        print("second :", second.val)
        

    # print("first: ",first.val)
    # print("second: ", second.val)
    # Step 3: Remove the Kth last node
    second.next = second.next.next

    # Return updated head (dummy.next skips over dummy)
    return dummy.next



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
    print((' -> ').join(str(val) for val in result))



values = [1,2,4,7]
k = 1
head = create_linked_list(values)
print_linked_list(head)

print_linked_list(remove_kth_list_node(head, k))