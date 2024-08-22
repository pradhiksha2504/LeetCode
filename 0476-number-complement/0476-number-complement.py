class Solution:
    def findComplement(self, num: int) -> int:
        binary = format(num, 'b')
        binary = str(binary)
        binary = binary.replace("1","-")
        binary = binary.replace("0","+")
        binary = binary.replace("-","0")
        binary = binary.replace("+","1")

        return int(binary,2)