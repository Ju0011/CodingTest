def solution(numbers, hand):
    answer = ''
    a = {1:'L', 3:'R', 4:'L', 6:'R', 7:'L', 9:'R'}
    for i in numbers:
        if i in a:
            answer += a[i]



    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))