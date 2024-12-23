from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        duplicate_count = defaultdict(lambda: {'row': {}, 'col': {}})
        boxes = [(0,3), (3,6), (6,9)]
        for i in range(len(boxes)):
            row_range = boxes[i]
            for j in range(len(boxes)):
                col_range = boxes[j]

                box_counts = defaultdict(lambda: 0)                
                for row_idx in range(row_range[0], row_range[1]):
                    for col_idx in range(col_range[0], col_range[1]):
                        item = board[row_idx][col_idx]
                        if item == ".": continue 
                        
                        # check duplicate in box
                        if box_counts[item] >= 1: return False
                        box_counts[item] += 1

                        # check row
                        if row_idx in duplicate_count[item]['row']: return False
                        duplicate_count[item]['row'][row_idx] = 1

                        # check column
                        if col_idx in duplicate_count[item]['col']: return False
                        duplicate_count[item]['col'][col_idx] = 1
        
        return True


if __name__ == '__main__':
    answer = Solution()

    board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    answer_1 = answer.isValidSudoku(board)
    print(f"Result for test case 1: {answer_1}")

    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    answer_2 = answer.isValidSudoku(board)
    print(f"Result for test case 1: {answer_2}")
