class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        q = []
        m, n = len(board), len(board[0])
        visited = [[0]*n for _ in range(m)]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i in range(m):
            if board[i][0] == "O":
                q.append([i, 0])
            if board[i][n-1] == "O":
                q.append([i, n-1])
        
        for j in range(n):
            if board[0][j] == "O":
                q.append([0, j])
            if board[m-1][j] == "O":
                q.append([m-1, j])

        while q:
            i, j = q.pop(0)
            visited[i][j] = 1

            for dirs in directions:
                a, b = i+dirs[0], j+dirs[1]

                if a>=0 and b>=0 and a<m and b<n and board[a][b] == "O" and visited[a][b] == 0:
                    q.append([a, b])
        
        for i in range(m):
            for j in range(n):

                if board[i][j] == "O" and visited[i][j] == 0:
                    board[i][j] = "X"
        
        return
