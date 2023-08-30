class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    dummy = ListNode(0)  # Create a dummy node to handle edge cases
    dummy.next = head
    prev = dummy
    curr = head
    
    while curr and curr.next:
        next_node = curr.next
        curr.next = next_node.next
        next_node.next = curr
        prev.next = next_node
        prev = curr
        curr = curr.next
    
    return dummy.next

# Example usage
# Construct the linked list: 1 -> 2 -> 3 -> 4
linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
new_head = swapPairs(linked_list)
# The linked list after swapping pairs: 2 -> 1 -> 4 -> 3
