class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sort(head):
    if not head or not head.next:
        return head

    mid = get_middle(head)
    right_head = mid.next
    mid.next = None
    left_sorted = merge_sort(head)
    right_sorted = merge_sort(right_head)

    return merge(left_sorted, right_sorted)


def get_middle(head):
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(left, right):
    dummy = ListNode()
    tail = dummy

    while left and right:
        if left.val < right.val:
            tail.next, left = left, left.next
        else:
            tail.next, right = right, right.next
        tail = tail.next

    tail.next = left or right
    return dummy.next