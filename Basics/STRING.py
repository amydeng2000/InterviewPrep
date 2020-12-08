# CLARIFYING Q's
"""
- ASCII or Unicode? There are 128 characters in ASCII, 256 in unique ASCII
- White space?
- Case sensitive?
- Non alphabetic/numeric chars?
"""

# METHODS
"""
- s.isalnum()  -> returns True if the string only contains alphabetic & numeric chars
- s.lower()
- s[start:end] -> slicing doesn't error if start or end > len(s)
- s.index(c) -> position of first index
"""

# TRICKS
"""
- ans[::2], ans[1::2] = feed[(len+1)/2:], feed[:(len+1)/2]  -> interleaving strings
- check if s2 is one insertion away from s1:
    - fast but long: iterate through s1 s2 at the same time, increase s2's pointer if different, flag if you've seen difference twice +
    - slower but short: for i in len(s2), check if s2[:i]+s2[i+1:] == s1
- check if s2 is one replacement away from s1: iterate through both strings, use a flag to track if already found difference
- check if s2 is s1 rotated: check if s1 is a substring of s2*2, because if x1 = xy, x2 = yx, yxyx should contain xy
"""

# ITERATE through strings
s1 = "abcd"
# direct
for letter in s1:
    print(letter)
# convert into array
arr = list(s1)
result = "".join(arr)  # 'abcd'
# Split by white space
s = "a b "
l = s.split() # default split is by white space['a', 'b']


# STRING BUILDER
letters = ['a','m','y']
name = ""
for l in letters:
    name += l  
# each time it creates a new copy, slow runtime! Use the list() and .join() functions instead



# STRING <=> INT
num = 1
string = str(1)
new_num = int(string)



# STRING COMPARISON
'a' == 'a'  # True
"abc" == "abc"  # True
