def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    thr = [3,3,1,1,2,2,4,4,5,5]
    
    one_1 = one*(int(len(answers)/len(one)))+one[:len(answers)%len(one)]
    two_1 = two*(int(len(answers)/len(two)))+two[:len(answers)%len(two)]
    thr_1 = thr*(int(len(answers)/len(thr)))+thr[:len(answers)%len(thr)]
    
    
    result = [0,0,0]
    for i in range(len(answers)):
        if one_1[i] == answers[i]:
            result[0] += 1
    for i in range(len(answers)):
        if two_1[i] == answers[i]:
            result[1] += 1
    for i in range(len(answers)):
        if thr_1[i] == answers[i]:
            result[2] += 1
    m = max(result)
    
    return [i+1 for i,v in enumerate(result) if v==m]
