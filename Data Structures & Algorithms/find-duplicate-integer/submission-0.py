class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)
        
        for idx, val in hashmap.items():
            if val > 1:
                return idx