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
            if self.dfs(i, prerequisites, mem, True) == False: 
                return False
        return True
    
    def dfs(self, course, prerequisites, mem, flag):
        mem.append(course)
        for p in prerequisites:
            if not flag: return False
            if p[0] == course:
                print(p[1])
                print(mem)
                if p[1] in mem: 
                    flag = False
                    return False
                return self.dfs(p[1], prerequisites, mem, flag)
        return flag

s = Solution()
prereq = [[0,1], [1,0]]
print(s.canFinish(2, prereq))