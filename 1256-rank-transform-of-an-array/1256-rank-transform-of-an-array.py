class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(list(set(arr)))
        value= {}
        for i in range(len(a)):
            value[a[i]] = i+1

        for i  in range(len(arr)):
            arr[i] = value[arr[i]]
        return  arr
        