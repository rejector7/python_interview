class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_set = ['(', '[', '{']
        right_set = [')', ']', '}']
        for bracket in s:
            if bracket in left_set:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                b = stack.pop()
                if bracket != right_set[left_set.index(b)]:
                    return False
                else:
                    continue
        if len(stack) == 0:
            return True
        return False
