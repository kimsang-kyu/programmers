def solution(priorities, location):
    lst = [(p, i) for (i, p) in enumerate(priorities)]
    count = 0           
    
    while lst:
        hold = lst.pop(0)
        if lst:
            lst_1 = [priority for priority, idx in lst]
        
        if lst_1:
            if hold[0] >= max(lst_1):
                if hold[1] == location:
                    return count + 1
                else:
                    count += 1
            else:
                lst.append(hold)
