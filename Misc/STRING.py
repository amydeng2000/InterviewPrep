# CLARIFYING Q's
"""
- ASCII or Unicode? There are 128 characters in ASCII, 256 in unique ASCII
- White space?
- Case sensitive?
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




print(int('9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999'))