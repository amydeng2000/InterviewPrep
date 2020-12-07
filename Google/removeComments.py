class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        seenBlockOpen = False
        res = []
        for line in source:
            i = 0
            if not seenBlockOpen:
                code = []
            while i < len(line):
                if line[i:i+2] == "//" and not seenBlockOpen:
                    break
                elif line[i:i+2] == "/*" and not seenBlockOpen: 
                    seenBlockOpen = True
                    i += 1
                elif line[i:i+2] == "*/" and seenBlockOpen: 
                    seenBlockOpen = False
                    i += 1
                elif not seenBlockOpen:
                    code.append(line[i])
                i += 1
            if code and not seenBlockOpen:
                res.append("".join(code))
        return res
                    
            