# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        mid = count // 2
        temp = head
        i = 1
        while temp and i < mid:
            temp = temp.next
            i += 1
        # print(temp.val)
        delete = temp.next
        temp.next = delete.next
        # print(temp.val, delete.val)
        delete.next = None
        
        return head
