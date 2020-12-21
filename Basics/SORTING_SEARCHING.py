# ALGO's
"""
- Merge Sort
- Quick Sort
- Radix Sort: large array, small ranges of values

- Binary Search
"""

# Merge Sort in place
def mergeSort(arr):
    # Terminating cases - if singular elem array, return
    if len(arr) > 1:
        # Find mid, mergeSort both half
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)  # mergeSort is in place
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:           # MANY Q's ALTERNATE THE COMPARISON HERE
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Tail case
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

arr = [1,6,3,7,0,4,2,8]
mergeSort(arr)
print(arr)


# BINARY SEARCH: O(log N) runtime
def binarySearch(arr, x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == x: return mid   # MANY Q's ALTERNATE COMPARISON HERE
        if arr[mid] < x: low = mid+1   # OR CHANGE BOUNDARIES DIFFERENTLY
        else: high = mid-1
    return -1  # element not in array


        
