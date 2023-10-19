class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        def update(board, r, c):
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return

            neighbors = [(i, j) for i in range(r-1, r+2) for j in range(c-1, c+2) 
                        if -1 < i < len(board) and -1 < j < len(board[0]) and (i, j) != (r, c)]
            
            mine_count = [board[i][j] for i,j in neighbors].count("M")
            
            if mine_count == 0:
                board[r][c] = 'B'
                for i,j in neighbors: 
                    if board[i][j] == "E":
                        update(board, i, j)
            else:
                board[r][c] = str(mine_count)
            
        update(board, click[0], click[1])
        return board