"""
https://leetcode.com/problems/min-stack/description/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack) == 0:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) == 0:
            return
        p = self.stack.pop()
        if p >= 0:
            return self.min + p
        else:
            res = self.min
            self.min -= p
            return res

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return
        top = self.stack[len(self.stack) - 1]
        if top > 0:
            return self.min + top
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Test code
ms = MinStack()
ms.push(-1)
print ms.top()
print ms.getMin()
