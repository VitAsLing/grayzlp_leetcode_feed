"""
https://leetcode.com/problems/simplify-path/description/

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        slash_start = 0
        i = 1
        while i < len(path):
            if path[i] == '/':
                if i == slash_start + 1:
                    slash_start += 1
                    i += 1
                    continue
                else:
                    stack.append(path[slash_start + 1:i])
                    slash_start = i
                    i += 1
            else:
                i += 1
        if i - (slash_start + 1) > 0:
            stack.append(path[slash_start + 1:i])

        res = []
        for s in stack:
            if s == '..':
                if len(res) > 0:
                    res.pop()
            elif s == '.':
                continue
            else:
                res.append(s)
        part = ''
        for r in res:
            part += '/' + r
        if part == '':
            part = '/'
        return part


# Test code
print Solution().simplifyPath("/.../")
