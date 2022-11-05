# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""class Node:
    def__init__(self, data):
        self.data = data
        self.next = None"""
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr = ListNode()
        temp = head
        
        amount = 0
        
        while temp:
            temp = temp.next
            amount += 1
        
        temp = head  
        amount = int(amount/2)
        
        
        while temp:
            if amount > 0:
                temp = temp.next
                amount -= 1
                #print(amount)
            elif amount == 0:
                ptr = temp
                #print(temp.val)
                return ptr
                temp = temp.next
                amount -= 1
            
        #print(output)
        return output
