# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp.next:
            sec = temp.next
            gcd = math.gcd(temp.val, sec.val)

            newnode = ListNode(gcd)
            temp.next = newnode
            newnode.next = sec
            temp = sec
        return head
        