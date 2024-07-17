class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        values = [chr(i) for i in range(97,123)]
        key = key.replace(" ","")
        keys = ""
        for i in key:
            if i not in keys:
                keys+=i
        f = {k:v for k,v in zip(keys,values)}
        output = ""
        for i in message:
            if i == " ":
                output += " "
            else:
                output += f[i]
        return output
