from queue import PriorityQueue


class Solution(object):
    def kthSmallest(self, matrix, k):
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        priority_queue = PriorityQueue()
        for h in heap:
            priority_queue.put(h)

        ret = 0
        for _ in range(k):
            ret, i, j = priority_queue.get()

            if j + 1 < len(matrix[0]):
                priority_queue.put((matrix[i][j + 1], i, j + 1))

        return ret


matrix = [
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8

print(Solution().kthSmallest(matrix, k))
