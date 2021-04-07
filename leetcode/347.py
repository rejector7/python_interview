from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1
        num_tuple_list = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(num_tuple_list[i][0])
        return res