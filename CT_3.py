def solution(queue1, queue2):
    q = queue1 + queue2
    num = sum(q) // 2

    output1, input1 = 0, len(queue1)-1
    queue1_sum = sum(queue1)
    count = 0

    while output1 < len(q) and input1 < len(q):        
        if queue1_sum == num :
            return count

        elif queue1_sum < num and input1 < len(q)-1:
            input1 += 1
            queue1_sum += q[input1]

        else:
            queue1_sum -= q[output1]
            output1 += 1

        count += 1

    return -1

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

print(solution(queue1, queue2))