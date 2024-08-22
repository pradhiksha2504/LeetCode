class Solution:
    def findComplement(self, num: int) -> int:
        binary = format(num, 'b')
        binary = list(str(binary))
        for i in range(len(binary)):
            if binary[i] == "1":
                binary[i] = "0"
            else:
                binary[i] = "1"
        binary= "".join(map(str, binary))

        return int(binary,2)