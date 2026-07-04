# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp1=list1
        while temp1:
            arr.append(temp1.val)
            temp1=temp1.next
        temp2=list2
        while temp2:
            arr.append(temp2.val)
            temp2=temp2.next
        arr.sort()
        if not arr:
            return None
        dummy=ListNode(0)
        curr=dummy
        for value in arr:
            curr.next=ListNode(value)
            curr=curr.next
        return dummy.next