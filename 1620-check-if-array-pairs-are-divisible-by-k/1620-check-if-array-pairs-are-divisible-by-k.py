class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem = {}
        for i in arr:
            x = i % k
            if x in rem:
                rem[x] += 1
            else:
                rem[x] = 1
        print(rem)
        if 0 in rem:
            if rem[0]% 2 != 0:
                return False
        for i, j  in rem.items():
            if i == 0:
                continue
            if k-i in rem:
                if j != rem[k-i]:
                    return False
            else:
                return False

        return True
