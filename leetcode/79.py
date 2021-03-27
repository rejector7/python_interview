from copy import deepcopy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def search(i: int, j: int, suffix:str) -> bool:
            if len(suffix) == 0:
                return True
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            if board[i][j] != suffix[0]:
                return False
            temp = board[i][j]
            board[i][j] = '*'
            if search(i+1, j, suffix[1:]) or search(i-1, j, suffix[1:]) or search(i, j+1, suffix[1:]) or search(i, j-1, suffix[1:]):
                return True
            board[i][j] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(i, j, word):
                        return True
        return False

