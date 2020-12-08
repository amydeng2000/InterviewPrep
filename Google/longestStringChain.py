from collections import defaultdict
class Solution(object):
    # def longestStrChain(self, words):
    #     dp = {}
    #     for w in sorted(words, key=len):
    #         dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in xrange(len(w)))
    #     return max(dp.values())
    
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = defaultdict(list)
        for w in words:
            d[len(w)].append(w)
                
        def dfs(pred): # outputs length of longest chain starting from w
            if pred in dp: return dp[pred]
            longest = 0
            for w in d[len(pred)+1]:
                if is_pred(pred, w):
                    longest = max(dfs(w), longest)
            dp[pred] = longest+1
            return dp[pred]
        
        def is_pred(w1, w2):
            i = j = 0
            diff = False
            while i < len(w1) and j < len(w2):
                if w1[i] != w2[j]:
                    if diff:
                        return False
                    j += 1
                    if j >= len(w2) or w1[i] != w2[j]:
                        return False
                    diff = True
                i += 1
                j += 1
            return True
            # for i in range(len(w2)):
            #     if w2[:i]+w2[i+1:] == w1: return True
            # return False
        
        longest = 0
        dp = {}
        for pred in words:
            longest = max(dfs(pred), longest)
        return longest

            
            
            
        