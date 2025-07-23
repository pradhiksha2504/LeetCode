class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        def remove_pair(s, first, second, val):
            score = 0
            stack = []
            for i in s:
                if stack and stack[-1] == first and i == second:
                    score += val
                    stack.pop()
                else:
                    stack.append(i)
            return "".join(stack), score
        
        if x > y:
            s, val = remove_pair(s, "a", "b", x)
            score += val
            _, val = remove_pair(s, "b", "a", y)
            score += val
        else:
            s, val = remove_pair(s, "b", "a", y)
            score += val
            _, val = remove_pair(s, "a", "b", x)
            score += val
        
        return score