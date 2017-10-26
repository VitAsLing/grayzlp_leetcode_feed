"""
https://leetcode.com/problems/word-ladder/description/

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the
code definition to get the latest changes.

"""
from time import time


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        reached = set()
        reached.add(beginWord)
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        dist = 1
        while endWord not in reached:
            to_add = set()
            for each in reached:
                char_list = list(each)
                for i in range(len(char_list)):
                    prev_char = char_list[i]
                    for j in range(ord('a'), ord('z') + 1):
                        char_list[i] = chr(j)
                        candidate = ''.join(char_list)
                        if candidate in wordList:
                            to_add.add(candidate)
                            wordList.remove(candidate)
                    char_list[i] = prev_char
            dist += 1
            if not len(to_add):
                return 0
            reached = to_add
        return dist

    def ladderLength2(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        to_visit = []
        self.add_next(beginWord, wordList, to_visit)
        dist = 2
        while len(to_visit) > 0:
            num = len(to_visit)
            for i in range(0, num):
                word = to_visit.pop()
                if word == endWord:
                    return dist
                self.add_next(word, wordList, to_visit)
            dist += 1
        return 0

    def add_next(self, word, candidates, to_visit):
        if word in candidates:
            candidates.remove(word)
        char_list = list(word)
        for i in range(len(char_list)):
            prev_char = char_list[i]
            for j in range(ord('a'), ord('z') + 1):
                char_list[i] = chr(j)
                next = ''.join(char_list)
                if next in candidates:
                    to_visit.insert(0, next)
                    candidates.remove(next)
            char_list[i] = prev_char


# Test code
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
start = time()
print Solution().ladderLength(beginWord, endWord, wordList)
print time() - start
