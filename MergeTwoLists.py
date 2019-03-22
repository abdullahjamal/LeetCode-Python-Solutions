# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        newlist = mergelist = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                mergelist.next = l1
                l1 = l1.next
            else:
                mergelist.next = l2
                l2 = l2.next
            
            mergelist = mergelist.next
        mergelist.next = l1 or l2
        return newlist.next
        
            
        
        
