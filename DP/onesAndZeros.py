class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        mem = {}
        return self.helper(strs, len(strs)-1, m, n, mem)
    
    def count(self, string):
        m = n = 0
        for s in string:
            if s == '0':
                m += 1
            else:
                n += 1
        return m, n
        
    def helper(self, strs, i, m, n, mem):
        if i < 0: return 0
        if (i, m, n) in mem: return mem[(i, m, n)]
        k, p = self.count(strs[i])
        mem[(i, m, n)] = self.helper(strs, i-1, m, n, mem)
        if k <= m and p <= n:
            mem[(i, m, n)] = max(mem[(i, m, n)], 1+self.helper(strs, i-1, m-k, n-p, mem))
        return mem[(i, m, n)]
