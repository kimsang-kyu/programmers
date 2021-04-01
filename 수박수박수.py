def solution(n):
    a = '수박'
    subak = a*(int(n/len(a)))+a[:n%len(a)]
    return subak
  
  
  
#다른사람풀이

#def solution(n):
#  a = '수박'*n
#  return a[:n]

# 쉬운코드긴 하지만 연산량이 많아져서 비효율적이다.
