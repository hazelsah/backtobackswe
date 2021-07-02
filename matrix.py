import numpy as np

class Solution:
    def rotate(self, matrix):
        '''
        :type matrix: list of list of int
        :rtype: list of list of int
        '''
        tr_matrix = np.transpose(matrix)
        for i in range(len(tr_matrix)):
            i_size = len(tr_matrix)
            for j in range(int(len(tr_matrix[i]) / 2)):
                temp = tr_matrix[i][i_size - 1 - j]
                tr_matrix[i][i_size - 1 - j] = tr_matrix[i][j]
                tr_matrix[i][j] = temp
        print(tr_matrix)

    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp
        print(matrix)


if __name__ == '__main__':
    s = Solution()
    s.rotate(
        [
            [10, 20],
            [30, 40]
        ])
