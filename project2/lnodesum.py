class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = 0
        b = 0
        l3 = ListNode(0)
        k = 0
        p = False
        while l1 is not None:
            a = a + l1.val*pow(10,k)
            k = k+1
            l1 = l1.next
        k = 0
        while l2 is not None:
            b = b + l2.val*pow(10,k)
            k = k+1
            l2 = l2.next
        c = a+b
        l3.val = c%10
        c = c//10
        if c//10 !=0:
            p = ListNode(c)
            l3.next = p
        while p:
            p.val = c%10
            c = c//10
            if c!=0:
                q = ListNode(c)
                p.next = q
            p = p.next
        return l3

s = Solution()
