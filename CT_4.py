from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()

    boat = deque(people)

    while boat:

        if len(boat) < 2:
            if boat[0] <= limit:
                boat.pop()
                answer += 1
        
        else :
            if boat[0] + boat[-1] > limit:
                boat.pop()
                answer += 1

            else:
                boat.pop()
                boat.popleft()
                answer += 1


    return answer

people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))