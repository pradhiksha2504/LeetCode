class Solution:
    def minimumPushes(self, word: str) -> int:
        hm = [0] * 26
        for i in word:
            hm[ord('a')-ord(i)] += 1
        hm = sorted(hm, reverse = True)
        count = 0
        char= 0
        for j in hm:
            count +=j * ((char // 8)+1)
            char += 1
        return count
        