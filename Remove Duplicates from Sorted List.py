# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        #print(head)
        
        if temp == None:
            return head
        
        tempnext = temp.next
        
        while tempnext:
            
            if temp.val == tempnext.val:
                temp.next = tempnext.next
                tempnext = tempnext.next
            else:
                temp = temp.next
                tempnext.next
        #print(head)
        return head

        
