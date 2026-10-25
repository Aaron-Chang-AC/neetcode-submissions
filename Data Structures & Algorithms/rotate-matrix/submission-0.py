class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # element diagonal swap
        for i in range(n):
            x_l, y_l = i, 0
            x_r, y_r = 0, i

            while x_l > x_r and y_l < y_r and x_l * x_r * y_l * y_r >= 0:
                matrix[x_l][y_l], matrix[x_r][y_r] = matrix[x_r][y_r], matrix[x_l][y_l]
                x_l, y_l = x_l - 1, y_l + 1
                x_r, y_r = x_r + 1, y_r - 1
        
        for i in range(n - 1, 0, -1):
            x_l, y_l = n - 1, i
            x_r, y_r = i, n - 1

            while x_l > x_r and y_l < y_r and x_l * x_r * y_l * y_r >= 0:
                matrix[x_l][y_l], matrix[x_r][y_r] = matrix[x_r][y_r], matrix[x_l][y_l]
                x_l, y_l = x_l - 1, y_l + 1
                x_r, y_r = x_r + 1, y_r - 1
        # flip 
        for i in range(n):
            x_l, y_l = i, 0
            x_r, y_r = i, n - 1

            while y_l < y_r:
                matrix[x_l][y_l], matrix[x_r][y_r] = matrix[x_r][y_r], matrix[x_l][y_l]
                x_l, y_l = x_l, y_l + 1
                x_r, y_r = x_r, y_r - 1
        return

'''
1 2 3
4 5 6
7 8 9

element diagonal swap
1 4 7
2 5 8
3 6 9

flip
7 4 1
8 5 2
9 6 3
'''