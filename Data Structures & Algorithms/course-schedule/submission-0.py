class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites_adj = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            prerequisites_adj[course].append(prerequisite)
        
        canBeCompleted, exploring = set(), set()

        def dfs(course):
            if course in exploring:
                return False
            
            if course in canBeCompleted:
                return True
            
            exploring.add(course)

            for prerequisite in prerequisites_adj[course]:
                if not dfs(prerequisite):
                    return False

            exploring.remove(course)
            canBeCompleted.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True