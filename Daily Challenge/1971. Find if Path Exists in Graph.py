class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        deque = collections.deque([source])

        while deque:
            currentNode = deque.popleft()

            if currentNode == destination:
                return True

            visited.add(currentNode)

            for neighbor in graph[currentNode]:
                if neighbor not in visited:
                    deque.append(neighbor)

        return False
