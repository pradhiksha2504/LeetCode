class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # if numBottles < numExchange:
        #     return numBottles
        # elif numBottles == numExchange:
        #     return 1 + numBottles
        count = 0
        n = numBottles
        while numBottles >= numExchange:
            count += 1
            numBottles = (numBottles - numExchange) + 1
        return count + n        
        # return (numBottles-1) // (numExchange-1) + numBottles
        