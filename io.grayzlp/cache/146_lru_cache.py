"""
https://leetcode.com/problems/lru-cache/description/

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:
get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it
should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

"""


class DLinkedNode(object):
    def __init__(self):
        self.key = -1
        self.value = -1
        self.pre = None
        self.post = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.post = self.tail
        self.tail.pre = self.head
        self.dict = {}
        self.count = 0
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict.keys():
            return -1
        else:
            node = self.dict[key]
            self.move_to_first(node)
            return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.dict.keys():
            node = DLinkedNode()
            node.key = key
            node.value = value

            self.add_node(node)
            self.count += 1
            self.dict[key] = node

            while self.count > self.capacity:
                remove_node = self.pop_tail()
                del self.dict[remove_node.key]
                self.count -= 1
        else:
            node = self.dict[key]
            node.value = value
            self.move_to_first(node)

    def add_node(self, node):
        node.pre = self.head
        node.post = self.head.post

        self.head.post.pre = node
        self.head.post = node

    def remove_node(self, node):
        pre = node.pre
        post = node.post

        pre.post = post
        post.pre = pre

    def pop_tail(self):
        pop = self.tail.pre
        self.remove_node(pop)
        return pop

    def move_to_first(self, node):
        self.remove_node(node)
        self.add_node(node)


# Test code
cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print cache.get(1)
cache.put(3, 3)
print cache.get(2)
cache.put(4, 4)
print cache.get(1)
print cache.get(3)
print cache.get(4)
