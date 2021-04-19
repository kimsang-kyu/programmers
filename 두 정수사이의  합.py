def solution(a, b):
    list = sorted([a,b])
    answer = 0
    for i in range(list[0],list[1]+1):
        answer += i
    return answer
