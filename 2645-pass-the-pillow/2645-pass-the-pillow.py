class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n :
            count = 1
            for i in range(time):
                count += 1
            return count
        else:
            count = 1
            for i in range(1,time+1):
                count = (count + 1)
                if count == 0:
                    count = 2
                if count == n:
                    count = -1*n
            return abs(count)

        