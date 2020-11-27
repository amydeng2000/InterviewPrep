class Solution(object):
    # prerequisites = [[take_after, take_before]]
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        print(0 in [0, 1])
        for i in range(numCourses):
            mem = []
            if self.dfs(i, prerequisites, mem) == False: 
                return False
        return True
    
    def dfs(self, course, prerequisites, mem):
        mem.append(course)
        flag = True
        for p in prerequisites:
            if p[0] == course:
                if p[1] in mem: 
                    return False
                flag = flag and self.dfs(p[1], prerequisites, mem)
        return flag