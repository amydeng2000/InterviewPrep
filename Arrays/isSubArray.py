# Return True if arr2 is a subarray of arr1
def subarray(arr1, arr2):
    if len(arr1) == 0: 
        return False
    if len(arr2) == 0:
        return True
    p1 = 0
    while p1 < len(arr1):
        p2 = 0
        if arr1[p1] == arr2[p2]: 
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] != arr2[p2]: 
                    break
                p1 += 1
                p2 += 1
            if p2 == len(arr2):
                return True
        p1 += 1
    return False

arr1 = ['a', 'b', 'c', 'd']
arr2 = ['c', 'e']

print(subarray(arr1, arr2))