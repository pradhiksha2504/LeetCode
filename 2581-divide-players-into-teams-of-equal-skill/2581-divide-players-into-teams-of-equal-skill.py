class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill)-1
        res = skill[l]+skill[r]
        output = skill[l]*skill[r]
        while l < r-1:
            print(res,output)
            l += 1
            r -= 1
            if skill[l]+skill[r] == res:
                output += skill[l]*skill[r]
                pass
            else:
                return -1
        return output
        
            
        