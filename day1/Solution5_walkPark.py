# 시뮬레이션 - 공원산책
def solution(park, routes):
    X = 0
    Y = 0

    mapParkList = []
    for str in park:
        mapParkList.append(list(str))

    for i in range(len(mapParkList)):
        for j in range(len(mapParkList[i])):
            if mapParkList[i][j] == 'S':
                X = i
                Y = j



    answer = []
    return answer

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))