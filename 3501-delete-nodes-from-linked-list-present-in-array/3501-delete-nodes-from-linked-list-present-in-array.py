# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        while head and head.val in nums:
            head = head.next  

        if not head:
            return None
        
        temp, prev = head.next, head
        while temp:
            if temp.val not in nums:
                prev.next =  temp
                prev = temp
            temp = temp.next
        prev.next = None
        return head
