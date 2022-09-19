def solution(arr):
    num = max(arr)
    num_ori = num
    arr.remove(num)

    while True:
        for i in range(len(arr)):
            if num % arr[i] != 0:
                break
            
        else:
            return num
        num += num_ori

arr = [2,6,8,14]
print(solution(arr)) 