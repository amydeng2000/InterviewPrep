"""
Two Pointer
- used to find pairs in a sorted array (twoSum, 3Sum)
"""

"""
Sliding Window
- Fixed window: sum up the first k elements; in a for loop, add the latest, subtract the earliest, compare metrics
    - Sometimes required to keep track of the metrics
    - exp: keep track of median requires insertion, deletion methods to keep track of the sorted curr window
- Non-fixed window: find a contiguous subarray that ...
    - find the first contiguous subarray that meets/violates the condition
    - remove oldest element until condition voilated/met, observe new window and update maxVal, then move the right pointer up until condition met/violates, repeat
- Multiple Window:
    - "Throtlling Gateway" hackerrank: given requestTimes = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,11,11,11,12,12,12], we have to drop requests acording to rules
    - every second, number of requests <= 3; every 10 seconds (inclusive of both ends), number of requests <= 20; every 60 seconds, #requests <= 60
    - sol1: slide three windows across, each of size 4, 21, 61. If the len=4 window contain all the same index, drop
    - sol2: utilize indecies. if i>=20 and requestTies[i] - requestTimes[i-20] < 10: drop i
"""


# TRICKS
"""
- how to keep a nonlocal variable that every recursive call can mutate/add to? 
    - do self.var =  
    - Lists are default to be nonlocal 
"""