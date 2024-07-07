class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles < numExchange:
            return numBottles
        elif numBottles == numExchange:
            return 1 + numBottles
        count = 0
        n = numBottles
        while numBottles >= numExchange:
            count += 1
            numBottles = (numBottles - numExchange) + 1
        return count + n
        # count = numBottles // numExchange
        # remain = count + (numBottles % numExchange)
        # new = 0
        # if remain < numExchange:
        #     return numBottles + count
        # while remain >= numExchange:
        #     new += 1
        #     remain -= numExchange
        #     if new + remain >= numExchange:
        #         count = count + 1 + new
        #         remain -= new
        #         new = 0
        # print(new, count, remain)
        # return numBottles + count + new
        # remain = numBottles % numExchange
        # full = numBottles // numExchange
        # now = remain + full
        # count = now // numExchange
        # now = now % numExchange
        # # while now >= numExchange:
        # #     count += 1
        # #     now -= numExchange
        # if count + now > numExchange:
        #     count += ((count+now)//numExchange) + 1
        # print(full,count,now)
        # return numBottles + full + count
        # n = numBottles
        # while numBottles > 0:
        #     full  += 1
        #     numBottles -= numExchange
        # count = 0
        # if full >= numExchange:
        #     count = full // numExchange
        # print(count,full,numBottles)
        # if count == 0:
        #     if numBottles == -1:
        #         return n + full
        #     return n + full - 1
        # return numBottles + n + full + count
        # return (numBottles-1) // (numExchange-1) + numBottles
        