class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        new = [0]
        for i in range(len(gain)):
            new.append(sum(gain[:i+1]))
        print(new)
        return max(new)
