class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        w1 = list(set(word1))
        w2 = list(set(word2))
        if sorted(w1) != sorted(w2):
            return False
        f1 = Counter(word1)
        f2 = Counter(word2)
        if sorted(f1.values()) == sorted(f2.values()):
            return True
        