def solution(nums):
    num_set = len(set(nums))
    N = len(nums) / 2

    if N > num_set:
        return num_set
    else:
        return int(N)

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]))