class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        sum_set = set()
        sum_set.add(n)
        while n != 1:
            s = str(n)
            sum = 0
            for cha in s:
                sum += int(cha) ** 2
            if sum in sum_set:
                return False
            sum_set.add(sum)
            n = sum
        return True