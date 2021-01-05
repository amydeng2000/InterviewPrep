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
"""