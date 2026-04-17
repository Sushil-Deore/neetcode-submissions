class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        value_count = {}

        for i in nums:
            value_count[i] = 1 + value_count.get(i, 0)
        
        return sorted(value_count.keys(), key = lambda x : value_count[x], reverse = True)[:k]