class Solution:
    def maxTotalFruits(self, fruits, startPos, k):
        n = len(fruits)
        ans = 0
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + fruits[i][1]

        left = 0
        for right in range(n):
            # current fruit range is from fruits[left][0] to fruits[right][0]
            while left <= right:
                left_pos = fruits[left][0]
                right_pos = fruits[right][0]

                min_steps = min(
                    abs(startPos - left_pos) + (right_pos - left_pos),
                    abs(startPos - right_pos) + (right_pos - left_pos)
                )

                if min_steps > k:
                    left += 1
                else:
                    break

            if left <= right:
                total = prefix[right+1] - prefix[left]
                ans = max(ans, total)

        return ans
