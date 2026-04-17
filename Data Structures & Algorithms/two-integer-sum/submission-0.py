class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for idx, v in enumerate(nums):
            diff = target - v
            if diff in hashmap:
                return [hashmap[diff], idx]
            hashmap[v] = idx
