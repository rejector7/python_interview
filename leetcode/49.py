from collections import defaultdict
class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     # L = [chr(i) for i in range(97, 123)]
    #     res = defaultdict(list)
    #     for s in strs:
    #         res[tuple(sorted(s))].append(s)
    #     return list(res.values())
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # L = [chr(i) for i in range(97, 123)]
        res = defaultdict(list)
        for s in strs:
            cha_count = [0] * 26
            for cha in s:
                cha_count[ord(cha) - ord('a')] += 1
            res[tuple(cha_count)].append(s)
        return list(res.values())

