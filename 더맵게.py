'''
정답은 출력하지만 효율성이 떨어짐
def solution(scoville, K):
    count = 0
    while min(scoville) < K:
        if len(scoville) > 1:
            scoville.sort()
            scoville.append(scoville.pop(0) + (scoville.pop(0) * 2))
        else:
            -1
        count += 1
    return count
'''
# https://www.daleseo.com/python-heapq/
import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < k:
        if len(scoville) > 1:
            min_1 = heapq.heappop(scoville)
            min_2 = heapq.heappop(scoville) * 2
            heapq.heappush(scoville, min_1 + min_2)
            count += 1
        else:
            return -1
    return count
