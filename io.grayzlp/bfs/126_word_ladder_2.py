"""
https://leetcode.com/problems/word-ladder-ii/description/

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""
import string
import sys
import time

import collections


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        level = {beginWord}
        parents = collections.defaultdict(set)
        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                for char in string.ascii_lowercase:
                    for i in range(len(beginWord)):
                        n = node[:i] + char + node[i + 1:]
                        if n in wordList and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p] + r for r in res for p in parents[r[0]]]
        return res

    # This solution will cause TimeLimitExceeded, but it is brilliant
    # It is worked in c++ because string is mutable, but immutable in python
    def findLadders2(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(wordList)
        ladder = {}
        for word in word_set:
            ladder[word] = sys.maxint
        if endWord not in word_set:
            return []
        prev_ladder = {}
        queue = [beginWord]
        min = sys.maxint
        ladder[beginWord] = 0
        while len(queue) > 0:
            word = queue.pop()
            dist = ladder[word] + 1
            if dist > min:
                break
            char_list = list(word)
            for k in range(0, len(word)):
                prev = char_list[k]
                for j in range(ord('a'), ord('z') + 1):
                    char_list[k] = chr(j)
                    new_word = ''.join(char_list)
                    if new_word in ladder.keys():
                        if ladder[new_word] < dist:
                            continue
                        if ladder[new_word] == dist:
                            if new_word in prev_ladder.keys():
                                prev_ladder[new_word].append(word)
                            else:
                                prev_ladder[new_word] = [word]
                        else:
                            ladder[new_word] = dist
                            prev_ladder[new_word] = [word]
                            queue.insert(0, new_word)
                    if new_word == endWord:
                        min = dist
                char_list[k] = prev
        ans = []
        self.dfs(ans, [], prev_ladder, beginWord, endWord)
        return ans

    def dfs(self, res, part, prev_ladder, start, current):
        part.insert(0, current)
        if current == start:
            res.append(list(part))
        else:
            for ladder in prev_ladder[current]:
                self.dfs(res, part, prev_ladder, start, ladder)
        part.pop(0)


begin = "hit"
end = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

start = time.time()
print Solution().findLadders(begin, end, words)
print time.time() - start
