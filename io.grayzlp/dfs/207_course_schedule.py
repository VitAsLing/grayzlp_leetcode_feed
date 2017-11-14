"""
https://leetcode.com/problems/course-schedule/description/

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed
as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you
should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph
is represented.You may assume that there are no duplicate edges in the input prerequisites.
click to show more hints.

Hints:
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering
exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological
Sort.
Topological sort could also be done via BFS.

"""


class Solution(object):
    # BFS
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = self.build_graph_reverse(numCourses, prerequisites)
        degrees = self.compute_degrees(graph)
        for i in range(0, numCourses):
            for j in range(0, numCourses):
                if degrees[j] == 0:
                    break
            else:
                return False
            degrees[j] = -1
            for neigh in graph[j]:
                degrees[neigh] -= 1
        return True

    def build_graph_reverse(self, num, prerequisites):
        graph = [[] for i in range(0, num)]
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
        return graph

    def compute_degrees(self, graph):
        degrees = [0 for i in range(0, len(graph))]
        for neighbors in graph:
            for neighbor in neighbors:
                degrees[neighbor] += 1
        return degrees

    # DFS
    def canFinish2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = self.build_graph(numCourses, prerequisites)
        visited = [False for i in range(numCourses)]
        on_path = [False for i in range(numCourses)]
        for node in range(numCourses):
            if not visited[node] and self.dfs_cycle(node, graph, visited, on_path):
                return False
        return True

    def build_graph(self, num, prerequisites):
        graph = [[] for i in range(0, num)]
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])
        return graph

    def dfs_cycle(self, node, graph, visited, on_path):
        on_path[node] = visited[node] = True
        for neighbor in graph[node]:
            if on_path[neighbor] or self.dfs_cycle(neighbor, graph, visited, on_path):
                return True
        on_path[node] = False
        return False


# Test code
p1 = [[0, 1], [1, 2], [2, 3], [3, 0]]
p2 = [[0, 1], [1, 2], [2, 3]]
print Solution().canFinish(4, p1)
print Solution().canFinish(4, p2)
