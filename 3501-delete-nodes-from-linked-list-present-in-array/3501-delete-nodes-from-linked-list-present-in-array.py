# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        nums = set(nums)
        while head and head.val in nums:
            head = head.next
        temp = ListNode(0)
        temp = head
        while temp:
            if temp.val in nums:
                temp = head
                while temp.next:
                    if temp.next.val in nums:
                        delete = temp.next
                        temp.next = delete.next
                        delete.next = None
                        del delete
                    else:
                        if temp:
                            temp = temp.next
                if temp.val in nums:
                    temp = head
                    while temp.next:
                        prev = temp
                        temp = temp.next
                    prev.next = None
                    temp = None

            if temp:
                temp = temp.next
        return head
                
