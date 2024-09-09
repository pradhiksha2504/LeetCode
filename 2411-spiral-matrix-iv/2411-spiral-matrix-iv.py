# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for i in range(n)]for j in range(m)]
        # print(matrix)
        temp = head
        rowbeg, rowend, colbeg, colend = 0, m, 0, n
        while temp and rowbeg < rowend and colbeg < colend:
            for i in range(colbeg, colend):
                # ans.append(matrix[rowbeg][i])
                if not temp:
                    break
                matrix[rowbeg][i] = temp.val
                # print(rowbeg, i)
                # print("matrix:", matrix)
                temp = temp.next
            for j in range(rowbeg+1, rowend-1):
                if not temp:
                    break
                matrix[j][colend-1] = temp.val
                temp = temp.next
            
            if rowend != rowbeg+1:
                for i in range(colend-1, colbeg-1, -1):
                    if not temp:
                        break
                    # ans.append()
                    matrix[rowend-1][i] = temp.val
                    temp = temp.next
            if colend != colbeg+1:
                for j in range(rowend-2, rowbeg, -1):
                    if not temp:
                        break
                    # ans.append(matrix[j][colbeg])
                    matrix[j][colbeg] = temp.val
                    temp = temp.next
            
            rowbeg += 1
            rowend -= 1
            colbeg += 1
            colend -= 1

        return matrix