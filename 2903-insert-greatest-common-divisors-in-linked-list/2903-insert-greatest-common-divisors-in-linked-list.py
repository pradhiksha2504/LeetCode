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
            n1 = temp.val
            n2 = sec.val
            # print(n1, n2)
            gcd = math.gcd(n1, n2)

            newnode = ListNode(gcd)
            temp.next = newnode
            newnode.next = sec
            temp = sec
        return head
        