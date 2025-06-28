class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Build a simple list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
