"""
https://leetcode.com/problems/clone-graph/description/

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

"""


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        return self.clone(node, {})

    def clone(self, node, processed):
        if not node:
            return None
        if node.label in processed.keys():
            return processed[node.label]
        clone_node = UndirectedGraphNode(node.label)
        processed[clone_node.label] = clone_node
        for each in node.neighbors:
            clone_node.neighbors.append(self.clone(each, processed))
        return clone_node


# Test code
n1 = UndirectedGraphNode(1)
n2 = UndirectedGraphNode(2)
n3 = UndirectedGraphNode(3)
n1.neighbors.append(n3)
n1.neighbors.append(n2)
n2.neighbors.append(n1)
n2.neighbors.append(n3)
n3.neighbors.append(n1)
n3.neighbors.append(n2)

node = Solution().cloneGraph(n1)
for each in node.neighbors:
    print each.label
