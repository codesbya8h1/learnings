class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head, k):
    dummy = ListNode(0)
    dummy.next = head
    prev_group_tail = dummy
    
    while head:
        print(display_list(head))
        group_start = head
        group_end = get_kth_node(head, k)
        
        
        if not group_end:
            break
        print("group start", display_list(group_start))
        next_group_start = group_end.next
        print("next group start", display_list(next_group_start))
        group_end.next = None
        
        prev_group_tail.next = reverse(group_start)
        print(display_list(prev_group_tail))
        group_start.next = next_group_start
        
        prev_group_tail = group_start
        head = next_group_start
    
    return dummy.next

def create_linked_list(nums):
    dummy = ListNode(0)
    curr  = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def get_kth_node(curr, k):
    while curr and k>1:
        curr = curr.next
        k = k -1
    return curr


def display_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


# Test the function
arr = [1, 2, 3, 4, 5]
k = 2

head = create_linked_list(arr)
result = reverse_k_group(head, k)
print(display_list(result))  # Output: [2, 1, 4, 3, 5]