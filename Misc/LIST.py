# DEQUE: fast appendleft() and popleft() comparing to list's insert(0, elem), pop(0)
from collections import deque 
# CREATE: iterables or empty
d1 = deque('abc')  # ['a', 'b', 'c']
d2 = deque([1,2,3])  # [1, 2, 3]
d3 = deque()
d3.append('second')
d3.appendleft('first')
d3.extend(['third', 'fourth'])  # d3 = ['first', 'second', 'third', 'fourth']
d3.pop()  # 'fourth'
d3.popleft()  # 'first'
reverse = deque(reversed(d3))  # ['third', 'second']
d3.clear()  # empty the que, d3 = []


# ARRAYS
arr1 = [1,3,2]
arr2 = list('123') # ['1', '2', '3']
# METHODS
