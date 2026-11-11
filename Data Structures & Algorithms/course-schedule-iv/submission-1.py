class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        pres = defaultdict(set)

        for prerequisite, course in prerequisites:
            adj[course].add(prerequisite)
            pres[course].add(prerequisite)
        
        def dfs(course: int, original: int, visit: set) -> None:
            if course in visit:
                return
            
            visit.add(course)
            if course != original:
                pres[original].add(course)

            for pre in adj.get(course, ()):
                if pre not in visit:
                    dfs(pre, original, visit)
        
        for course in range(numCourses):
            dfs(course, course, set())
        
        res = []

        for prerequisite, course in queries:
            if prerequisite in pres.get(course, ()):
                res.append(True)
            else:
                res.append(False)
        
        return res