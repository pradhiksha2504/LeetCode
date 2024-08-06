class Solution:
    def minimumPushes(self, word: str) -> int:
        hm = [0] * 26
        ind = ord('a')
        for i in word:
            hm[ind-ord(i)] += 1
        hm = sorted(hm, reverse = True)
        if 0 in hm:
            hm = hm[:hm.index(0)] 
        count = 0
        char= 0
        for j in hm:
            count +=j * ((char // 8)+1)
            char += 1
        return count
        