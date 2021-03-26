from collections import deque
class Solution:
    # def letterCombinations(self, digits: str) -> List[str]:
    #     if len(digits) == 0:
    #         return []
    #     letters_map = {
    #         '2': 'abc',
    #         '3': 'def',
    #         '4': 'ghi',
    #         '5': 'jkl',
    #         '6': 'mno',
    #         '7': 'pqrs',
    #         '8': 'tuv',
    #         '9': 'wxyz'
    #
    #     }
    #     pre = []
    #     pre.append("")
    #     res = []
    #     for digit in digits:
    #         for s in pre:
    #             for cha in letters_map[digit]:
    #                 res.append(s + cha)
    #         pre = res
    #         res = []
    #     return pre
    # def letterCombinations(self, digits: str) -> List[str]:
    #     if len(digits) == 0:
    #         return []
    #     letters_map = {
    #         '2': 'abc',
    #         '3': 'def',
    #         '4': 'ghi',
    #         '5': 'jkl',
    #         '6': 'mno',
    #         '7': 'pqrs',
    #         '8': 'tuv',
    #         '9': 'wxyz'
    #
    #     }
    #     res = deque()
    #     res.append("")
    #     for digit in digits:
    #         for i in range(len(res)):
    #             s = res.popleft()
    #             for cha in letters_map[digit]:
    #                 res.append(s + cha)
    #     return res
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        letters_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'

        }
        res = deque()
        res.append("")

        def moveToNext(index: int) -> None:
            if index == len(digits):
                return
            for i in range(len(res)):
                s = res.popleft()
                for cha in letters_map[digits[index]]:
                    res.append(s + cha)
            index += 1
            moveToNext(index)
        moveToNext(0)
        return res