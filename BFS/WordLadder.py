from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)  # because set removal time is N(1), list removal is N(n)
        if endWord not in wordList: return 0
        q = deque()
        q.append((1, beginWord))
        if beginWord in wordList: wordList.remove(beginWord)
        while q:
            level, curr = q.popleft()
            for i in range(len(curr)):
                for chidx in range(ord('a'), ord('z')+1):
                    c = chr(chidx)
                    nextW = curr[:i]+c+curr[i+1:]
                    if nextW in wordList:
                        if nextW == endWord: return level + 1
                        q.append((level+1, nextW))
                        wordList.remove(nextW)
        return 0

