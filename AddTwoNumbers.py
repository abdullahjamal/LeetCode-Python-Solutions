# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        newlist = sublist = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry +=l1.val
                l1 = l1.next
            if l2:
                carry+=l2.val
                l2 = l2.next
            
            carry,sum_ = divmod(carry,10)
            sublist.next = sublist = ListNode(sum_)
            
        return newlist.next
