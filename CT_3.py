def solution(queue1, queue2):
    q = queue1 + queue2
    num = sum(q) / 2
    queue1_sum = sum(queue1)
    count, inputnum, output = 0, len(queue1) - 1, 0

    while inputnum < len(q) and output < len(q) :
        if sum(queue1) == num and sum(queue2) == num :
            return count 
        
        elif sum(queue1) < num and inputnum < len(q)-1 :
            inputnum += 1
            queue1_sum  += q[inputnum]
        
        else :
            queue1_sum -= q[output]
            output += 1

        count += 1
    return -1

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

print(solution(queue1, queue2))