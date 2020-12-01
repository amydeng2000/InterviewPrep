# CHAIN MAP: combines multiple dictionaries to perform updates 
from collections import ChainMap
update = {"First":"Last", "Amy": "Deng","Mark": "Li"}
original = {"First":"Last Name", "Amy": "Denggg"}
d = ChainMap(update, original)  # Update comes first. 
for k, v, in d.items():
    print(k,v)
# First Last Name
# Amy Denggg
# Mark Li


# COUNTERS: rapid tallies. Pre-initialized count = 0
from collections import Counter
c = Counter()
print(c["blue"])  # print 0 instead of error
# CREATE counters from iterable(list/string), mapping, key words
c1 = Counter(["blue", "red", "green", "blue"])
c2 = Counter('abcba')
c3 = Counter({"a":2, "b":2, "c":-1})
c4 = Counter(a=2, b=2)  # keyword is not a string/expression
# METHODS
sortedList = sorted(c3.elements())  # ['a', 'a', 'b', 'b'], counts <=1 is ignored
c1.most_common()  # [('blue', 2), ('red', 1), ('green', 1)]
c1.most_common(1)  # [('blue', 2)]
c2.subtract(c3)
print(c2)  # {'c': 2, 'a': 0, 'b': 0}
