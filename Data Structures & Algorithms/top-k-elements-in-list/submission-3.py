class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for i in nums:
            if i not in res:
                res[i] = 1
            res[i] += 1
        return sorted(res.keys(), key = lambda x : res[x], reverse=True)[:k]