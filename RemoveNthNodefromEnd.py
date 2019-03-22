# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        
        def delete(head,n):
            if n == 0:
                return head.next
            count = 1
            head_temp = head
            while head and head.next:
                if n == count:
                    head.next = head.next.next
                head = head.next
                count +=1
            
            return head_temp
        
        count = 1
        head_temp = head
        
        while head and head.next:
            count += 1
            head = head.next
            
        del_ind = count - n
        
        list_ = delete(head_temp,del_ind)
        
        return list_
