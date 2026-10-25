class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        v = [set() for i in range(9)]
        h = [set() for i in range(9)]
        box = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':
                    continue
                
                if board[i][j] in v[j] or board[i][j] in h[i] or board[i][j] in box[int((i//3)*3 + j//3)]:
                    return False
                
                v[j].add(board[i][j])
                h[i].add(board[i][j])
                box[int((i//3)*3 + j//3)].add(board[i][j])
        
        return True