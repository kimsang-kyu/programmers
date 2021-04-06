def solution(array, commands):
    result = []
    for i in range(len(commands)):
        a = sorted(array[commands[i][0]-1:commands[i][1]])
        b = a[commands[i][2]-1]
        result.append(b)
    return result
