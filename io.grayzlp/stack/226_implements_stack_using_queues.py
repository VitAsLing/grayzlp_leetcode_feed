"""
https://leetcode.com/problems/implement-stack-using-queues/description/

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size,
and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or
deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if len(self.queue2) == 0:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        container_queue = self.queue1
        empty_queue = self.queue2
        if len(self.queue2) > 0:
            container_queue, empty_queue = empty_queue, container_queue
        while len(container_queue) > 1:
            res = container_queue.pop(0)
            empty_queue.append(res)
        return container_queue.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        res = self.pop()
        self.push(res)
        return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue1) | len(self.queue2) == 0


# Test code
st = MyStack()
st.push(1)
st.push(2)
st.push(3)
print st.pop()
print st.top()
print st.pop()
print st.empty()
print st.pop()
print st.empty()
