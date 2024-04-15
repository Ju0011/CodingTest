from collections import deque

def solution(prices):
    queue = deque(prices)   #deque([1, 2, 3, 2, 3])
    answer = []
    while queue:    #Q가 null이 아닐 때까지
        price = queue.popleft() # price = 1
        sec = 0
        for q in queue:
            sec += 1
            if price > q:   # 1 > 3 ,sec = 4    # 3 > 2, sec = 1
                break
        answer.append(sec)
    return answer

print(solution([1, 2, 3, 2, 3]))