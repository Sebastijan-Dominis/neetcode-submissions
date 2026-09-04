class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for course, pre in prerequisites:
            adj[course].append(pre)

        exploring = set()
        canBeCompleted = set()

        def dfs_completion_possibility(course: int):
            if course in exploring:
                return False

            if course in canBeCompleted:
                return True
            
            exploring.add(course)

            for pre in adj.get(course, ()):
                if not dfs_completion_possibility(pre):
                    return False
            
            exploring.remove(course)
            canBeCompleted.add(course)

            return True
        
        for course in range(numCourses):
            if not dfs_completion_possibility(course):
                return False
        
        return True