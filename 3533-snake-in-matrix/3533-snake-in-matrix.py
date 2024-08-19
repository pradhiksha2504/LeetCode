class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        pos = 0  
        for i in commands:
            if i=="UP":
                pos -= n  
            elif i=="RIGHT":
                pos += 1  
            elif i=="DOWN":
                pos += n  
            else:
                pos -= 1  

        return pos