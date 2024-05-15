# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp = head
        count = 0
        while temp:
            count+=1
            temp=temp.next
        for i in range(k%count):
            temp1 = None
            temp = head
            while temp.next:
                temp1 = temp
                temp = temp.next
            temp.next = head
            head = temp
            temp1.next = None
        return head