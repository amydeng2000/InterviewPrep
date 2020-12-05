from collections import Counter
from collections import OrderedDict
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        c = Counter(S)
        occur = sorted(c.most_common(), key=lambda x:x[1], reverse=True)
        k, v = occur[0]
        if v > len(S)-v+1: return ""
        charList = []
        for k, v in occur:
            charList.extend([k]*v)
        ans = [None]*len(S)
        ans[::2], ans[1::2] = charList[:(len(S)+1)/2], charList[(len(S)+1)/2:]
        return "".join(ans)