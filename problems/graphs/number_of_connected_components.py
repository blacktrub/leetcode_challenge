"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.
Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""


class Solution:
    def solution(self, n, edges) -> int:
        parent = list(range(n))

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(x, y):
            p1, p2 = find(x), find(y)
            parent[p2] = p1

        for x, y in edges:
            union(x, y)

        return len(set(parent))


if __name__ == "__main__":
    s = Solution()
    assert s.solution(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert s.solution(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
