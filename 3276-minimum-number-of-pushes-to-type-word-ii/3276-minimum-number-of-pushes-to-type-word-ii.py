class Solution:
    def minimumPushes(self, word: str) -> int:
        hm = {}
        for i in word:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
        hm = {k: v for k, v in sorted(hm.items(), key=lambda item: item[1],reverse = True)}
        count = 0
        char= 0
        for j in hm.values():
            count +=j * ((char // 8)+1)
            char += 1
        return count
        