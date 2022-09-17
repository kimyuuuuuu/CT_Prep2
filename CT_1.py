def solution(s):
    answer = []
    number = 1 #문자열의 갯수

    if len(s) == 1:
        return 1

    for i in range(1, (len(s)//2 + 1)):
        tmp = s[:i] #slice as n. maximum is half. 반복시마다 초기화 된다.
        other = "" #저장할 문자열

        for j in range(i, len(s)+i, i): #i부터 i만큼 건너뛰어서 끝까지 반복
            if tmp == s[j:i+j]: #다음 글자와 같으면
                number += 1 #숫자 추가

            else: #같지 않으면 -> 계산 시작
                if number != 1: #중복이 있었다. 
                    other += str(number)+tmp #단어 생성. ex) 2abc
                else:
                    other += tmp #단어 생성 ex) a. 하나짜리는 1안붙임.
                tmp=s[j:i+j] #
                number = 1 #숫자 초기화
        #print(other)

        answer.append(len(other))
        
    #return answer
    return min(answer)

s = input()
print(solution(s))