class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        column = len(board)
        row = len(board[0])
        wordItem = len(word)

        def dfs(x, y, st_ring, ind):

            if ind == wordItem:
                return 1
            if x < 0 or x >= column or y < 0 or y >= row:
                return 0

            if board[x][y] == -1:
                return 0
            if st_ring[ind] != board[x][y]:
                return 0
            
            temp = board[x][y]
            board[x][y] = -1
            
            top = bottom = left = right = 0

            bottom = dfs(x + 1, y, st_ring, ind + 1)
            right = dfs(x, y + 1, st_ring, ind + 1)
            left = dfs(x, y - 1, st_ring, ind + 1)
            top = dfs(x - 1, y, st_ring, ind + 1)
                
            board[x][y] = temp
            return left or right or bottom or top
        
        ind_arr = []

        for i in range(column):
            for j in range(row):
                if board[i][j] == word[0]:
                    ind_arr.append([i, j])
        
        for i in ind_arr:

            if dfs(i[0], i[1], word, 0):
                return 1

        return 0
        