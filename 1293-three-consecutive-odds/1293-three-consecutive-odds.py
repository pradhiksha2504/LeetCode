class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) == 3:
            if arr[0]%2!=0 and arr[1]%2!=0 and arr[2] % 2 != 0:
                return True
        else:
            for i in range(0,len(arr)-2):
                if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2] % 2 != 0:
                    return True
        