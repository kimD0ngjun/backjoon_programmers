def solution(board, moves):
    stack_board = [Stack() for _ in range(len(board))]
    basket = Basket()

    for i in range(len(board)):
        for j in range(len(board) - 1, -1, -1):
            doll = board[j][i]
            if doll != 0:
                stack_board[i].push(doll)

    for move in moves:
        temp = stack_board[move - 1].pop()

        if temp != -1:
            basket.push(temp)

    return basket.count

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

        return -1

class Basket:
    def __init__(self):
        self.items = []
        self.count = 0

    def push(self, item):
        if self.items:
            if item == self.items[-1]:
                self.items.pop()
                self.count += 2
                return

        self.items.append(item)

# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

