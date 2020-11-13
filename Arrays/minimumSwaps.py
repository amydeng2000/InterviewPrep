def minimumBribes(q):
    swaps = 0
    for i in range(len(q)):
        if q[i] > i + 3:
            print("Too chaotic")
            return
        start = max(0, q[i]-2)
        for j in range(start, i):
            if q[j] > q[i]:
                swaps += 1
    print(swaps)
    return 