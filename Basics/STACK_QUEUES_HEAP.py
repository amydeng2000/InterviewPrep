from collections import deque
# METHODS
"""
- d.append()
- d.pop()  -> pop right
- d.popleft()
- len(d)
"""

import heapq
# METHODS
"""
- heapq.heapify(list): turn list into min heap in place
- heapq.heappop(list): remove smallest element from heap
- heapq.heappush(list, elem): push the elem into heap
- maxHeap: multiply each element by -1 and store in minHeap. When you extract value, multiply by -1 again
"""
arr = [2,6,8,4,1,9,3]
heapq.heapify(arr)
print(arr)  # [1, 2, 3, 4, 6, 9, 8]s
smallest = heapq.heappop(arr)  # 1
heapq.heappush(arr, 5)  # push 5 into the heap
print(arr)  # [2, 4, 3, 8, 6, 9, 5]
