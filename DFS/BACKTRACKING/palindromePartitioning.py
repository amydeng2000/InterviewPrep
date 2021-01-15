class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # if reaches end, add currList + currElem to result []
        # generate substrings starting at i
        # if palindrome, append to curr list, call dfs
        
        currList = []
        result = []
        
        def dfs(i):
            if i > len(s)-1:
                result.append(currList[:])
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                if is_palindrome(sub):
                    currList.append(sub)
                    dfs(j)
                    currList.pop()
                    
        def is_palindrome(s):
            i = 0
            j = len(s)-1
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True
        
        dfs(0)
        return result