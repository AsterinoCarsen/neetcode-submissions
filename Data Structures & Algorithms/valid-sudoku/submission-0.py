class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = self.validRows(board)
        cols = self.validColumns(board)
        boxes = self.validBoxes(board)
        return rows and cols and boxes

    def validRows(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isUnique(row):
                return False
        return True

    def validColumns(self, board: List[List[str]]) -> bool:
        inverseBoard = [row[:] for row in board]
        for i in range(9):
            for j in range(9):
                inverseBoard[j][i] = board[i][j]
        
        return self.validRows(inverseBoard)

    def validBoxes(self, board: List[List[str]]) -> bool:
        for boxRow in range(3):
            for boxCol in range(3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[boxRow * 3 + i][boxCol * 3 + j])
                if not self.isUnique(box):
                    return False

        return True
    
    def isUnique(self, arr: List[str]) -> bool:
        filtered = [x for x in arr if x != "."]
        return len(set(filtered)) == len(filtered)
