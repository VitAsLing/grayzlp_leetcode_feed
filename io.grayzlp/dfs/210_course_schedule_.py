"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed
as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to
finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses,
return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order
is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1
and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering
is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph
is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""


class Solution(object):
    # BFS
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = self.build_graph_reverse(numCourses, prerequisites)
        degrees = self.build_degress(graph)
        res = []
        for i in range(numCourses):
            for j in range(numCourses):
                if degrees[j] == 0:
                    break
            else:
                return []
            degrees[j] -= 1
            res.append(j)
            for neighbor in graph[j]:
                degrees[neighbor] -= 1
        return res

    def build_graph_reverse(self, courses, prerequisites):
        graph = [[] for i in range(courses)]
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
        return graph

    def build_degress(self, graph):
        degrees = [0] * len(graph)
        for neighbors in graph:
            for neighbor in neighbors:
                degrees[neighbor] += 1
        return degrees

    # DFS
    def findOrder2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        visited = [False] * numCourses
        on_path = [False] * numCourses
        graph = self.build_graph(numCourses, prerequisites)
        print graph
        ans = []
        for i in range(numCourses):
            if not visited[i] and self.dfs(graph, on_path, visited, ans, i):
                return []
        return ans

    def build_graph(self, courses, prerequisites):
        graph = [[] for i in range(courses)]
        for item in prerequisites:
            graph[item[0]].append(item[1])
        return graph

    def dfs(self, graph, on_path, visited, res, node):
        if visited[node]:
            return False
        on_path[node] = visited[node] = True
        for neigh in graph[node]:
            if on_path[neigh] or self.dfs(graph, on_path, visited, res, neigh):
                return True
        on_path[node] = False
        res.append(node)
        return False


print Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
