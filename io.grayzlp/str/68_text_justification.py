"""
https://leetcode.com/problems/text-justification/description/

Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        index = 0
        while index < len(words):
            count = len(words[index])
            last = index + 1
            while last < len(words):
                if count + 1 + len(words[last]) > maxWidth:
                    break
                count += (1 + len(words[last]))
                last += 1
            if last == len(words) or last - index == 1:
                s = words[index]
                i = index + 1
                while i < last:
                    s = s + ' ' + words[i]
                    i += 1
                left_space = maxWidth - count
                while left_space > 0:
                    s = s + ' '
                    left_space -= 1
            else:
                slots_num = last - index - 1
                slots_space = (maxWidth - count + slots_num) / slots_num
                extra_num = (maxWidth - count + slots_num) % slots_num
                s = words[index]
                i = index + 1
                while i < last:
                    s = s + ' ' * slots_space
                    if extra_num > 0:
                        s = s + ' '
                        extra_num -= 1
                    s = s + words[i]
                    i += 1
            res.append(s)
            index = last
        return res


# Test code
print Solution().fullJustify(["a", "b", "c", "d", "e"], 3)
