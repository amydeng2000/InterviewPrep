from collections import defaultdict
def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    d = defaultdict(list)
    for i, j in prerequisites:
        d[i].append(j)
    seen = set()
    visited = [0]*numCourses
    order = []
    
    def check(course):
        if visited[course] == 1: return True
        if course in seen:
            return False
        seen.add(course)
        for c in d[course]:
            if not check(course): 
                print(2)
                return False
        seen.remove(course)
        visited[course] = 1
        order.append(course)
        return True
    
    for c in range(numCourses):
        if not check(c): return []
    return order


findOrder(2, [[1, 0]])