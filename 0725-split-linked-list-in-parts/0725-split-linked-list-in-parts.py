# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = [None]*k
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        print(length)
        minSize = length // k
        extra = length % k
        temp = head
        for i in range(k):
            res[i] = temp
            size = minSize + (1 if extra > 0 else 0)
            extra -= 1

            for j in range(size-1):
                if temp:
                    temp = temp.next
            if temp:
                nextNode = temp.next
                temp.next = None
                temp = nextNode
            

        return res


        