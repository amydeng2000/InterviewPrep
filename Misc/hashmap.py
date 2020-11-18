# Implement a new dictionary where you can add values to keys and vals
def hashMap(queryType, query):
    d = {}
    k = v = s = 0
    for qType, q in zip(queryType, query):
        if qType == "insert":
            d[q[0]-k] = q[1]-v
        elif qType == "addToValue":
            v += q[0]
        elif qType == "addToKey":
            k += q[0]
        elif qType == "get":
            s += d[q[0]-k]+v
    return s