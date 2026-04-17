class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''Start at the first element of the array with two variables: 
            one to track the current sum (current_sum) and 
            another to track the maximum sum seen so far (max_sum).
            For each element in the array:
            Decide whether to add it to your current_sum or 
            start fresh with this element alone, whichever is larger.
            Update max_sum if current_sum is now larger than max_sum.
            The final max_sum is the maximum sum of any 
            contiguous subarray.
        '''
        curr_sum = nums[0]
        max_sum = 0

        for i in nums:
            max_sum += i
            curr_sum = max(curr_sum, max_sum)
            if max_sum < 0:
                max_sum = 0
        return curr_sum

            