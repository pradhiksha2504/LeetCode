# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        temp = head
        while temp.next:
            new = temp.next
            while new:
                print(temp.val, new.val)
                if temp.val != new.val:
                    print("a", temp.val, new.val)
                    temp.next = new
                    break
                else:
                    if new.next is None:
                        print("new", new,temp)
                        temp.next = None
                        break
                new = new.next
            if temp.next:
                temp = temp.next
        return head

        