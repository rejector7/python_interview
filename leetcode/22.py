from collections import deque
class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
    #     left_bra = '('
    #     right_bra = ')'
    #     res = deque()
    #     res.append("")
    #     for _ in range(2 * n):
    #         for i in range(len(res)):
    #             pre = res.popleft()
    #             left = str(pre).count(left_bra)
    #             right = str(pre).count(right_bra)
    #             if left == right and left < n:
    #                 res.append(pre + left_bra)
    #             if left > right and left < n:
    #                 res.append(pre + left_bra)
    #                 res.append(pre + right_bra)
    #             if left == n:
    #                 res.append(pre + right_bra)
    #     return res
    def generateParenthesis(self, n: int) -> List[str]:
        left_bra = '('
        right_bra = ')'
        res = []
        def backtrack(s: str, left: int, right: int) -> None:
            if len(s) == 2 * n:
                res.append(s)
            if left < n:
                backtrack(s + left_bra, left + 1, right)
            if left > right:
                backtrack(s + right_bra, left, right + 1)
        backtrack('', 0, 0)
        return res