class Solution(object):
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        # create graph
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
            
        # visit each node
        for course in range(numCourses):
            if not self.dfs(graph, visited, course): return False
            
        return True
    
    def dfs(self, graph, visited, course):
        # if ith node is marked as being visited, then a cycle is found
        if visited[course] == -1: return False
        
        # if it is done visted, then do not visit again
        if visited[course] == 1: return True
        
        # mark as being visited
        visited[course] = -1
        
        # visit all the neighbours
        for prereq in graph[course]:
            if not self.dfs(graph, visited, prereq): return False
            
        # after visit all the neighbours, mark it as done visited
        visited[course] = 1
        
        return True
        