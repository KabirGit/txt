class Solution:
    def isSafe(self, board, row, col, n):
        # Check horizontally
        for j in range(n):
            if board[row][j] == 'Q':
                return False

        # Check vertically
        for i in range(n):
            if board[i][col] == 'Q':
                return False

        # Check left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check right diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def nQueen(self, board, row, n, ans):
        # Base case: if all rows are processed
        if row == n:
            ans.append(["".join(row) for row in board])  # Add the board to the result
            return

        for j in range(n):
            if self.isSafe(board, row, j, n):
                board[row][j] = 'Q'  # Place the queen
                self.nQueen(board, row + 1, n, ans)  # Recurse for the next row
                board[row][j] = '.'  # Backtrack

    def solveNQueens(self, n):
        board = [["." for _ in range(n)] for _ in range(n)]  # Initialize the board
        ans = []
        self.nQueen(board, 0, n, ans)
        return ans


# Main function
if __name__ == "__main__":
    sol = Solution()
    n = int(input("Enter the value of n: "))
    results = sol.solveNQueens(n)

    print("Solutions:")
    for solution in results:
        for row in solution:
            print(row)
        print()