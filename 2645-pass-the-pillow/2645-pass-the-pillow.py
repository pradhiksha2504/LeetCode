class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n :
            count = 1
            for i in range(time):
                count += 1
            return count
        else:
            # count = 1
            # t = 0
            # while time>t:
            #     curr += 1
            #     t += 1
            #     if curr == n:
            #         count  = 1
            #     if curr == 1:

            # rem = time % n
            # print(rem)
            # count = 1
            # quo = time // n
            # if quo % 2 != 0 :
            #     for i in range(rem+1):
            #         n -= 1
            #     return n
            # else:
            #     print("hi")
            #     for i in range(rem):
            #         count += 1
            #     return count
            count = 1
            for i in range(1,time+1):
                count = (count + 1)
                if count == 0:
                    count = 2
                print(i, count)
                if count == n:
                    count = -1*n
            return abs(count)
        # rem = time % n
        # return n - rem - 1
        