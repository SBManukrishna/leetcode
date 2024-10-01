# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next  
        ptr=slow.next    
        half=[]    
        while(ptr!=None):
            half.append(ptr.val)
            ptr=ptr.next
        half.reverse() 
        slow.next=None  

        print(head)
        print(half)

        seeker=head
        i=0
        while(i<len(half)):
            temp=seeker.next
            node1=ListNode(half[i])
            seeker.next=node1
            node1.next=temp
            i+=1
            seeker=seeker.next.next   
        