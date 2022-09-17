def solution(s):
    answer = []
    number = 1 #문자열의 갯수

    if len(s) == 1:
        return 1

    for i in range(1, (len(s)//2 + 1)):
        tmp = s[:i] #slice as n. maximum is half. 
        other = "" #save

        for j in range(i, len(s)+i, i): #Repeat by skipping by i
            if tmp == s[j:i+j]: #If it's the same as the next letter
                number += 1 #add number

            else: # !same
                if number != 1: # if duplication
                    other += str(number)+tmp #make word ex) 2abc
                else:
                    other += tmp 
                tmp=s[j:i+j] #Initialization
                number = 1 #Initialization
        #print(other)

        answer.append(len(other)) #during repeating, other's length append to answer
        
    #return answer
    return min(answer) #minimum

s = input()
print(solution(s))