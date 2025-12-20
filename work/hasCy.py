# Definition for singly-linked list.
# class ListNode(object):
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


head = ListNode(10)
head.next = ListNode(15)
head.next.next = ListNode(20)
head.next.next.next = head  

i = Solution()
print(i.hasCycle(head))
