def solution(n):
    a = '수박'
    subak = a*(int(n/len(a)))+a[:n%len(a)]
    return subak
  
  
  
#다른사람풀이
#def solution(n):
#  a = '수박'*n
#  return a[:n]
