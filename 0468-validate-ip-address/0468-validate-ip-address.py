class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def IPv6(IP):
            arr =  IP.split(":")
            if len(arr) != 8:
                return False
            for i in arr:
                if len(i) < 1 or len(i) > 4:
                    print(i)
                    return False
                try:
                    int(i)
                except:
                    for j in i:
                        if j.isdigit():
                            continue
                        if j not in "abcdefABCDEF":
                            return False
            return True
        def IPv4(s):
            arr = s.split(".")
            if len(arr) != 4:
                return False
            for i in arr:
                try:
                    x = int(i)
                except:
                    return False
                if (x <0  or x > 255):
                    return False
                if len(i) == 1 and i.isdigit():
                    continue
                else:
                    if i[0] == "0":
                        return False
            return True
                


        
        # print(nums)

        if IPv4(queryIP):
            return "IPv4"
        if IPv6(queryIP):
            return "IPv6"
        return "Neither"
        