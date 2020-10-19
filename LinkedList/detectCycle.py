class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not (fast and fast.next):
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast