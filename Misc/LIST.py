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
""" 
- .insert(i, x)
- .remove(x): remove the first occurance of x
- .pop(i)
- .index(x): return the first index 
- .count(x): return frequency
- .sort(arr, key=lambda x: expression(x), reverse=True): sort in place
- sorted(arr): returns a copy of a sorted array
"""
arr3 = sorted(arr1)  # arr3 = [1, 2, 3] this takes up extra space tho!!
arr1.sort()  # arr1 = [1, 2, 3]
arr2.reverse()  # arr2 = [3, 2, 1] reverse the elements in place, not reverse sort



# LIST COMPREHENSIONS
primes = [1,2,3,5,7,11]
l1 = [x**2 for x in primes if x**2 <= 50]
l2 = [x*y for x in primes for y in primes if x != y]



# SLICING
"""
arr [start: stop: step]
arr[::-1] reverses the list --> can be used to reverse string/num that get turned into string
"""



# ZIP & ENUMERATE
start = [1,3,5,8]
stop = [2,4,7,10]
list(zip(start, stop))  # [(1, 2), (3, 4), (5, 7), (8, 10)]
for start, stop in zip(start, stop):  # good for concise for loops
    print(start,stop)
items = ['pencil', 'notebook', 'key', 'wallet']
for i, x in enumerate(items):
    print(i,x)  # prints index and string pairs



# SET: unordered, constant lookup time b/c it's based on hashmap, eliminate duplicate elements
# CREATE with iterables
s1 = set([1,2,3,1])  # [1,2,3] elimiate duplicate 1
s2 = set('abc')
s3 = set()
# METHODS: add(), len(), elem in set
s3.add('a')
s3.add('2')
len(s3)  # 2

