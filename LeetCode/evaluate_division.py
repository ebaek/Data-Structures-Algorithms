# 399: Evaluate Division

from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        def buildGraph():
            for [(a, b), num] in zip(equations, values):
                graph[a][b] = num
                graph[b][a] = 1/num

        def bfs(query):
            start, end = query

            if start not in graph or end not in graph: return -1

            q = deque([(start, 1.0)])
            visited = set()

            while q:
                letter, prod = q.popleft()
                visited.add(letter)

                if letter == end: return prod

                for neighbor, val in graph[letter].items():
                    if neighbor in visited: continue
                    q.append((neighbor, prod*val))

            return -1

        buildGraph()
        return [bfs(query) for query in queries]
