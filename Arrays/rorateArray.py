def rotLeft(a, d):
    rot = d % len(a)
    cut = rot - 1
    arr = a[cut+1:]
    print(arr)
    arr.extend(a[:cut+1])
    return arr

print(rotLeft([1,2,3,4,5], 4))
