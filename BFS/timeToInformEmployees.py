from collections import deque, defaultdict

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        
        # counting how many levels are in a tree - BFS
        # process one level at a time by iterating through all nodes in the queue
        # processing nodes -> go through manager list, add subbordinates to new queue
        
        d = defaultdict(list)  # key=manager, value=subbordinate
        for i in range(len(manager)):
            d[manager[i]].append(i)
        
        q = deque()
        q.append(headID)
        time = [0 for _ in range(n+1)]
        time[headID] = 0
        while q:
            m = q.popleft()
            for sub in d[m]:
                q.append(sub)
                time[sub] = informTime[m] + time[m]
        return max(time)
                        
                        
        