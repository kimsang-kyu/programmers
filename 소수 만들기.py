from itertools import combinations
def solution(nums):
    ls = []
    for i in list(combinations(nums,3)):
        ls.append(sum(i))
    
    result = 0
    for i in ls:
        count = 0 
        for j in range(2,i-1):
            if int(i % j) == 0:
                count += 1
            if count > 0:
                break
        if count == 0:
            result += 1
    return result
