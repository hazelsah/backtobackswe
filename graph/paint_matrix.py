class Solution:
    def paint(self, image, row, col, newColor):
        '''
        :type image: list of list of int
        :type row: int
        :type col: int
        :type newColor: int
        :rtype: list of list of int
        '''

        seen = []
        sol = []
        queue = []

        seen.append((row, col))
        queue.append((row, col))

        while len(queue) > 0:
            cell = queue.pop(0)
            sol.append(cell)
            upper_limit = len(image) - 1
            lower_limit = 0

            if cell[0] + 1 <= upper_limit:
                if (cell[0] + 1, cell[1]) not in seen and mat[cell[0] + 1][cell[1]] != newColor:
                    queue.append((cell[0] + 1, cell[1]))
                    seen.append((cell[0] + 1, cell[1]))
            if cell[0] - 1 >= lower_limit:
                if (cell[0] - 1, cell[1]) not in seen and mat[cell[0] - 1][cell[1]] != newColor:
                    queue.append((cell[0] - 1, cell[1]))
                    seen.append((cell[0] - 1, cell[1]))
            if cell[1] + 1 <= upper_limit:
                if (cell[0], cell[1] + 1) not in seen and mat[cell[0]][cell[1] + 1] != newColor:
                    queue.append((cell[0], cell[1] + 1))
                    seen.append((cell[0], cell[1] + 1))
            if cell[1] - 1 >= lower_limit:
                if (cell[0], cell[1] - 1) not in seen and mat[cell[0]][cell[1] - 1] != newColor:
                    queue.append((cell[0], cell[1] - 1))
                    seen.append((cell[0], cell[1] - 1))

        for i in sol:
            image[i[0]][i[1]] = new
        return image


if __name__ == '__main__':
    s = Solution()
    mat = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]]
    print(mat)
    row = 0
    col = 1
    new = 1
    sol = s.paint(mat, row, col, new)
    print(sol)
