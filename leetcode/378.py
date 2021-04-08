import heapq
import sys


class Solution:
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     heap = []
    #     # m = len(matrix)
    #     n = len(matrix[0])
    #     for row in range(len(matrix)):
    #         heapq.heappush(heap, (matrix[row][0], row, 0))
    #     while k > 1:
    #         num, temp_row, temp_col = heapq.heappop(heap)
    #         if temp_col < n - 1:
    #             heapq.heappush(heap, (matrix[temp_row][temp_col + 1], temp_row, temp_col + 1))
    #         k -= 1
    #     return heap[0][0]
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                cur = -matrix[i][j]
                if len(heap) < k:
                    heapq.heappush(heap, cur)
                elif heap[0] < cur:
                    heapq.heappushpop(heap, cur)
                else:
                    break
        return -heap[0]

            
                



