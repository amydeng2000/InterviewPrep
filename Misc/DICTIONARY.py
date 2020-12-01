# # CHAIN MAP: combines multiple dictionaries to perform updates 
# from collections import ChainMap
# update = {"First":"Last", "Amy": "Deng","Mark": "Li"}
# original = {"First":"Last Name", "Amy": "Denggg"}
# d = ChainMap(update, original)  # Update comes first. 
# for k, v, in d.items():
#     print(k,v)
# # First Last Name
# # Amy Denggg
# # Mark Li


# # COUNTERS: rapid tallies. Pre-initialized count = 0
# from collections import Counter
# c = Counter()
# print(c["blue"])  # print 0 instead of error
# # CREATE counters from iterable(list/string), mapping, key words
# c1 = Counter(["blue", "red", "green", "blue"])
# c2 = Counter('abcba')
# c3 = Counter({"a":2, "b":2, "c":-1})
# c4 = Counter(a=2, b=2)  # keyword is not a string/expression
# # METHODS
# sortedList = sorted(c3.elements())  # ['a', 'a', 'b', 'b'], counts <=1 is ignored
# c1.most_common()  # replacement for .items() method, [('blue', 2), ('red', 1), ('green', 1)]
# c1.most_common(1)  # [('blue', 2)]
# c2.subtract(c3)
# c2  # {'c': 2, 'a': 0, 'b': 0}



# DEFAULTDICT: create the first instance for you, all else the same as dict
from collections import defaultdict
s1 = ['a', 'b', 'c', 'a']
d1 = defaultdict(int)  # value type
for letter in s1:
    d1[letter] += 1
d1  # {'a': 2, 'b': 1, 'c': 1}
s2 = [('a', 1), ('b', 2), ('c', 3), ('a', 2)]
d2 = defaultdict(list)
for k, v in s2:
    d2[k].append(v)
d2  # {'a': [1, 2], 'b': [2], 'c': [3]}



# ORDEREDDICT: remember the sequence in which you put in the k,v pairs
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od.popitem()  # ('c', 3)
list(od.items())[0]  # ('a', 1) NEED to put it in a list first.
# cnt.most_common() is itself a list, od or dictionary's .item() is still an dict_items object,
# thus is required to be put into a list first before indexing
