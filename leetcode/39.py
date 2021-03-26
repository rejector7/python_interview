class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        if len(candidates) == 0:
            return []
        if len(candidates) == 1:
            if target % candidates[0] == 0:
                return [[candidates[0]] * (target//candidates[0])]
            else:
                return []
        if target < candidates[0]:
            return []
        if target == candidates[0]:
            return [[candidates[0]]]
        res0 = self.combinationSum(candidates, target - candidates[0])
        for i in range(len(res0)):
            res0[i] = [candidates[0]] + res0[i]
        res1 = self.combinationSum(candidates[1:], target)
        return res0 + res1