class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for course, prerequisite in prerequisites:
            adj[course].append(prerequisite)
        
        visited, visiting = set(), set()
        output = []

        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)

            for pre in adj.get(course, ()):
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return output