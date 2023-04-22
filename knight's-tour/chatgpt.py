class KnightTour:
    def __init__(self, n, start_pos, end_pos):
        self.n = n
        self.board = [[-1 for i in range(n)] for j in range(n)]
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.moves = [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]

    def solve(self):
        self.board[self.start_pos[0]][self.start_pos[1]] = 0
        if self._solve_helper(self.start_pos[0], self.start_pos[1], 1):
            self.print_board()
        else:
            print("No solution found")

    def _solve_helper(self, row, col, move):
        if move == self.n**2:
            return True

        for i, j in self.moves:
            next_row = row + i
            next_col = col + j
            if self._is_valid_move(next_row, next_col):
                self.board[next_row][next_col] = move
                if self._solve_helper(next_row, next_col, move+1):
                    return True
                self.board[next_row][next_col] = -1
        return False

    def _is_valid_move(self, row, col):
        return row >= 0 and row < self.n and col >= 0 and col < self.n and self.board[row][col] == -1

    def print_board(self):
        for row in self.board:
            print(row)

if __name__ == '__main__':
    n = int(input("Enter the size of the board: "))
    start_row, start_col = map(int, input("Enter the starting position (row col): ").split())
    end_row, end_col = map(int, input("Enter the ending position (row col): ").split())
    same_start_end = input("Do you want the ending position to be the same as the starting position? (y/n) ")
    if same_start_end.lower() == 'y':
        end_row, end_col = start_row, start_col

    kt = KnightTour(n, (start_row, start_col), (end_row, end_col))
    kt.solve()