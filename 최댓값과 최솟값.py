def solution(s):
    s = s.replace(" ",",")
    lst = []
    for nr in s.split(','):
        lst.append(int(nr))
    return str(min(lst))+" "+str(max(lst))
