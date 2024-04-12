def solution(board, moves):
    count = 0
    stack = []

    for move in moves:
        X = 0
        Y = move-1
        print(f"move = {move}")
        print(f"Y = {Y}")
        print(f"X = {X}")
        while board[X][Y] == 0:
            X += 1
        print(f"new_X = {X}")
        stack.append(board[X][Y])
        print(board[X][Y])

        board[X][Y] = 0

        print("=======================")

    print(f"stack = {stack}")

    return count

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
               , [1,5,3,5,1,2,1,4]))