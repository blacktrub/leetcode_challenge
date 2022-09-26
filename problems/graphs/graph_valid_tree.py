"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
For example:
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Hint:
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree? According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.” Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together inedges.

"""

from typing import List


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n < 2

        parent = list(range(n))
        rank = [1] * n

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(x, y):
            p1, p2 = find(x), find(y)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for x, y in edges:
            if not union(x, y):
                return False

        root = find(0)
        for x in range(n):
            if find(x) != root:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True
    assert s.valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False
    assert s.valid_tree(2, []) == False
    assert s.valid_tree(1, []) == True
    assert s.valid_tree(3, [[0, 1]]) == False
    assert (
        s.valid_tree(8, [[0, 1], [1, 2], [3, 2], [4, 3], [4, 5], [5, 6], [6, 7]])
        == True
    )
