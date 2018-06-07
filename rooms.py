class Solution:
    def wallsAndGates(self, rooms):
        def traverse(row_i, col_i, distance):
            if row_i is len(rooms) or col_i is len(rooms[0]) or row_i < 0 or col_i < 0 or rooms[row_i][col_i] < distance:
                return -1

            room = rooms[row_i][col_i]

            if room is -1:
                return -1
            else:
                rooms[row_i][col_i] = distance

                traverse(row_i - 1, col_i, distance + 1)
                traverse(row_i + 1, col_i, distance + 1)
                traverse(row_i, col_i - 1, distance + 1)
                traverse(row_i, col_i + 1, distance + 1)

        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                # BFS from the zero rooms.
                if rooms[row][col] is 0:
                    traverse(row, col, 0)


Solution().wallsAndGates(
    [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
)
