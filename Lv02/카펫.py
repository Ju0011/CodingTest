def solution(brown, yellow):


    sq = brown + yellow # 전체 갯수

    sq_list = []

    for i in range(3,(sq//2)+1):
        if sq%i == 0:
            sq_list.append((i,int(sq/i)))

    for i in sq_list:
        if (i[0]-2) * (i[1]-2) == yellow:
            answer = [i[1],i[0]]
            break


    return answer


# def solution(brown, yellow):
#     for i in range(1, yellow +1):
#         if (yellow % i == 0):
#             yellow_row = int(yellow / i)
#             yellow_col = i
#             if (2 * (yellow_row + yellow_col) + 4 == brown):
#                 return [yellow_row +2, yellow_col+2]