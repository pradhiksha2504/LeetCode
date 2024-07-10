class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        x,y,z=0,1,2
        n = len(arr)
        while x<n and y<n and z<n:
            if arr[x] % 2 != 0:
                if arr[y] % 2 != 0:
                    if arr[z] % 2 != 0:
                        return True
            x += 1
            y += 1
            z += 1

        # if len(arr) == 3:
        #     if arr[0]%2!=0 and arr[1]%2!=0 and arr[2] % 2 != 0:
        #         return True
        # else:
        #     for i in range(0,len(arr)-2):
        #         if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2] % 2 != 0:
        #             return True
        