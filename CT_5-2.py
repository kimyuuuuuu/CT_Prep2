import numpy as np

def solution(numbers, hand):
    answer = ''
    keypad = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [11, 0, 12]])
    Left = [[3,0]]
    Right = [[3,2]]

    for i in numbers:
        index = np.where(keypad == i)

        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            Left = [[index[0], index[1]]]
            
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            Right = [[index[0], index[1]]]
        
        else : 
            l = abs(index[0] - Left[0][0]) + abs(index[1] - Left[0][1])
            r = abs(index[0] - Right[0][0]) + abs(index[1] - Right[0][1])

            if l < r :
                answer += 'L'
                Left = [[index[0], index[1]]]

            elif l > r:
                answer += 'R'
                Right = [[index[0], index[1]]]

            else : 
                if hand == "left" :
                    answer += 'L'
                    Left = [[index[0], index[1]]]
                
                else:
                    answer += 'R'
                    Right = [[index[0], index[1]]]

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1]
hand = 	"right"
print(solution(numbers, hand))