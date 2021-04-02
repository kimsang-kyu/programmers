def solution(numbers):
    result = []
    if len(numbers) >= 2 : 
        for i in range(len(numbers)):
            for j in numbers[i + 1:]:
                result.append((numbers[i]+j))
        list_1 = sorted(list(set(result)))        
    return list_1
