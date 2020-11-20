def outerSort(m):
    n = len(m)
    i = 0
    while i < n//2:
        arr = []
        arr.extend(m[i][i:n-i])
        arr.extend(m[n-i-1][i:n-i])
        for j in range(i+1, n-1-i):
            arr.append(m[j][i])
            arr.append(m[j][n-i-1])
        arr.sort()
        print(arr)
        for j in range(i, n-i):
            m[i][j] = arr.pop(0)
        print(arr)
        for j in range(i+1, n-1-i):
            m[j][n-i-1] = arr.pop(0)
        print(arr)    
        for j in reversed(range(i, n-i)):
            m[n-i-1][j] = arr.pop(0)
        print(arr)
        for j in reversed(range(i+1, n-1-i)):
            m[j][i] = arr.pop(0)
        print(m)
        i += 1



m = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
outerSort(m)