#https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

def solution(participant, completion):
    for p in participant:
        if participant.count(p) > completion.count(p):
                return p
