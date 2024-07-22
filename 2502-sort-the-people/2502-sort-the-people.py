class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict = {v:k for k,v in zip(names, heights)}
        output = []
        for i in sorted(dict.keys(), reverse = True):
            output.append(dict[i])
        return output
        