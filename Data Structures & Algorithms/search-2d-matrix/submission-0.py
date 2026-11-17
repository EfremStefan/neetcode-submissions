class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        while (left <= right):
            mid = left + (right - left) // 2
            mid_i, mid_j = mid // len(matrix[0]), mid % len(matrix[0])
            if(matrix[mid_i][mid_j] == target):
                return True
            elif matrix[mid_i][mid_j] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

        