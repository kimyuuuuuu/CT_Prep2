def solution(queue1, queue2):
    q = queue1 + queue2
    num = sum(q) / 2
    queue1_sum = sum(queue1)
    count, input, output = 0, len(queue1) - 1, 0

    while len(queue1) < len(q) and len(queue2) < len(q) :
        if sum(queue1) == num and sum(queue2) == num :
            return count 
        
        if sum(queue1) < num and input < len(q)  -1 :
            input += 1
            queue1_sum  += q[input]
        
        else :
            output += 1
            queue1_sum  -= q[output]
        
        count += 1
        
    return -1


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

print(solution(queue1, queue2))
