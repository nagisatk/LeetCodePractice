# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def flag(self, l3):
        if l3.val >= 10:
            l3.val = l3.val%10
            return 1
        return 0
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = ListNode(l1.val + l2.val)
        l3 = sum
        flag = self.flag(l3)
        l1 = l1.next
        l2 = l2.next
        while l1 is not None and l2 is not None:
            l3.next = ListNode(l1.val + l2.val + flag)
            flag = self.flag(l3.next)
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        while l1 is not None:
            l3.next = ListNode(l1.val + flag)
            flag = self.flag(l3.next)
            l1 = l1.next
            l3 = l3.next
        while l2 is not None:
            print l2.val
            l3.next = ListNode(l2.val + flag)
            flag = self.flag(l3.next)
            l2 = l2.next
            l3 = l3.next
        if flag:
            l3.next = ListNode(1)
        return sum
if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(5)
    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)
    sum = s.addTwoNumbers(l1, l2)
    while sum is not None:
        print sum.val,
        sum = sum.next