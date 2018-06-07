class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) is 0:
            return []

        i, j, count = 0, 0, 0
        rows, cols = len(matrix) - 1, len(matrix[0]) - 1
        arr, visited = [], [[False for a in range(rows + 1)] for b in range(cols + 1)]
        RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3

        # Start traversing right
        direction = RIGHT

        while count < (rows + 1) * (cols + 1):
            arr.append(matrix[i][j])
            visited[i][j] = True

            if direction is RIGHT:
                if j + 1 > cols or visited[i][j + 1]:
                    direction = DOWN
                    i += 1
                else:
                    j += 1
            elif direction is DOWN:
                if i + 1 > rows or visited[i + 1][j]:
                    direction = LEFT
                    j -= 1
                else:
                    i += 1
            elif direction is LEFT:
                if j - 1 < 0 or visited[i][j - 1]:
                    direction = UP
                    i -= 1
                else:
                    j -= 1
            elif direction is UP:
                if i - 1 < 0 or visited[i - 1][j]:
                    direction = RIGHT
                    j += 1
                else:
                    i -= 1

            count += 1

        return arr
