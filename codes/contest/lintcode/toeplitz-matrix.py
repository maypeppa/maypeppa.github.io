class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """

    def isToeplitzMatrix(self, matrix):
        # Write your code here
        n = len(matrix)
        m = len(matrix[0])

        def check_from(r, c):
            value = matrix[r][c]
            while r < n and c < m:
                v = matrix[r][c]
                if v != value:
                    return False
                r += 1
                c += 1
            return True

        for r in range(0, n):
            if not check_from(r, 0):
                return False
        for c in range(1, m):
            if not check_from(0, c):
                return False

        return True
