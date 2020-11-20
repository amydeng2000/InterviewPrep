def mergeStrings(s1, s2):
    l = r = 0
    d1 = d2 = {}
    result = []
    while l < len(s1) and r < len(s2):
        if not s1[l] in d1:
            d1[s1[l]] = s1.count(s1[l])
        if not s2[r] in d2:
            d2[s2[r]] = s2.count(s2[r])
        if d1[s1[l]] < d2[s2[r]]: 
            result.append(s1[l])
            l += 1
        elif d1[s1[l]] > d2[s2[r]]: 
            result.append(s2[r])
            r += 1
        elif s1[l] < s2[r]: 
            result.append(s1[l])
            l += 1
        elif s1[l] > s2[r]: 
            result.append(s2[r])
            r += 1
        else: 
            result.append(s1[l])
            l += 1
    if l < len(s1): result.append(s1[l:])
    elif r < len(s2): result.append(s2[r:])
    return "".join(result)
            
    

