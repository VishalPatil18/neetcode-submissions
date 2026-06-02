class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Input: matrix of integers, target int to find
        Output: Bool True if target found in matrix else False
        Plan:
            - have two variables lowRow and highRow
            - find midRow
            - check if Target exist in range of midRow or not
            - if Yes: Binary Search on that row
                    - if Found return True
                    - if not found in this row return False
            - if No: Check if Target > lastElement of midRow, lowRow = midRow + 1
            - if No: Check if Target < firstElement of midRow, highRow = midRow - 1
            - Do this until, lowRow <= highRow
        """
        # Variable Declaration
        lowRow = 0
        highRow = len(matrix) - 1

        while lowRow <= highRow:
            midRow = lowRow + (highRow - lowRow)//2
            if matrix[midRow][-1] < target:
                lowRow = midRow + 1
            elif matrix[midRow][0] > target:
                highRow = midRow - 1
            else:
                lowCol = 0
                highCol = len(matrix[midRow]) - 1
                while lowCol <= highCol:
                    midCol = lowCol + (highCol - lowCol)//2
                    if matrix[midRow][midCol] == target:
                        return True
                    elif matrix[midRow][midCol] < target:
                        lowCol = midCol + 1
                    else:
                        highCol = midCol - 1
                return False

        return False
