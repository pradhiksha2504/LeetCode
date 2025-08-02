class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        from collections import Counter

        count = Counter()
        for a, b in zip(basket1, basket2):
            if a != b:
                count[a] += 1
                count[b] -= 1

        excess = []
        for k, v in count.items():
            if v % 2 != 0:
                return -1
            excess.extend([k] * abs(v // 2))

        excess.sort()
        mini = min(min(basket1), min(basket2))
        n = len(excess) // 2
        return sum(min(2 * mini, excess[i]) for i in range(n))
