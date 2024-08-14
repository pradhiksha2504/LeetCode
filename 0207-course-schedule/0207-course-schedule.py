class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        visited = set()
        def dfs(curr):
            if curr in visited:
                return False
            if preMap[curr] == []:
                return True
            visited.add(curr)
            for course in preMap[curr]:
                if not dfs(course):
                    return False
            preMap[curr] = []
            visited.remove(curr)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        