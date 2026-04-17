class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum, maxsum = float("-inf"), nums[0]

        for n in nums:
            currsum = max(currsum, 0)
            currsum += n
            maxsum = max(maxsum, currsum)
        return maxsum