class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for course, pre in prerequisites:
            preMap[course].append(pre)
        visited = set()
        res = []
        print(preMap)
        def dfs(curr):
            if curr in visited:
                return False
            if preMap[curr] == []:
                if curr not in res:
                    print("hii")
                    res.append(curr)
                return True
            visited.add(curr)
            for course in preMap[curr]:
                print(preMap[curr], course)
                if dfs(course):
                    if course not in res:
                        print("hello")
                        res.append(course)  
                else:
                    return False
            if curr not in res:
                print("hoi")
                res.append(curr)
            visited.remove(curr)
            preMap[curr] = []
            return True

        for course in range(numCourses):
            if dfs(course):
                if course not in res:
                    res.append(course)
            else:
                return []
        return res

        