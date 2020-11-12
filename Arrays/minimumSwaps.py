def minimumBribes(q):
    swaps = 0
    for i in range(len(q)):
        if q[i] > i + 3:
            return "Too chaotic"
        elif q[i] > i+1:
            swaps += q[i] - (i+1)
    return swaps

print(minimumBribes([2,1,5,3,4]))