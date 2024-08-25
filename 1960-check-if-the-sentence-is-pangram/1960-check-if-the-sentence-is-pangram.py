class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        f = {}
        for i in sentence:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        return len(f.keys()) == 26