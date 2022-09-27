import heapq

def solution(operations) :
    min_numheap = []
    max_numheap = []

    for i in operations:
        if i[0] == 'I' :
            heapq.heappush(min_numheap, int(i[2:]))
            heapq.heappush(max_numheap, (-int(i[2:]), int(i[2:])))
        
        elif i[0] == 'D' and len(min_numheap) != 0:
            if i[2] == "1":
                heapq.heappop(max_numheap)
                min_numheap.pop()
            
            else :
                heapq.heappop(min_numheap)
                max_numheap.pop()

    if len(min_numheap) == 0 :
        return [0,0]
    
    else :
        min_numheap.sort()
        return [min_numheap[-1], min_numheap[0]]


operations = ["I 4", "I -1", "I 6", "I 3"]
print(solution(operations))