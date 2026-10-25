class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        starts = []
        self.res = False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    starts.append([i, j])
        
        visited = [[False]*n for _ in range(m)]

        def dfs(i, j, curr_word):
            if not curr_word:
                self.res = True

            if self.res or i<0 or j<0 or i>=m or j>=n or visited[i][j] or board[i][j] != curr_word[0]:
                return
            
            visited[i][j] = True
            next_word = curr_word[1:]

            dfs(i+1, j, next_word)
            dfs(i, j+1, next_word)
            dfs(i-1, j, next_word)
            dfs(i, j-1, next_word)

            visited[i][j] = False

            return
        
        for start in starts:
            dfs(start[0], start[1], word)
        
        return self.res
            
