import heapq

def solution(operations) :
    numheap = []

    for i in operations:
        if i[0] == 'I' :
            heapq.heappush(numheap, i[2:])
        
        elif i[0] == 'D' and len(numheap) != 0:
            if i[2] == '-':
                heapq.heappop(numheap)
            
            elif i[2] == '1':
                numheap = heapq.nlargest(len(numheap), numheap)
                heapq.heapify(numheap)
                #heapq.heappop(numheap)
                numheap = heapq.nsmallest(len(numheap), numheap)
            
        elif len(numheap) == 0 :
            continue
        
        print(numheap)

    if len(numheap) == 0 :
        return [0,0]
    
    else :
        return [numheap[-1], numheap[0]]


operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))