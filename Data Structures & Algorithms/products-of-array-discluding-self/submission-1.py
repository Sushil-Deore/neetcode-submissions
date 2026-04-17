class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = -i - 1
            print(f"i is {i} and j is {j}")
            l_arr[i] = l_mult
            print(f"l_arr[i] is {l_arr[i]} and l_mult is {l_mult}")
            r_arr[j] = r_mult
            print(f"r_arr[i] is {r_arr[i]} and r_mult is {r_mult}")
            l_mult *= nums[i]
            print(f"l_mult is {l_mult} and nums[i] is {nums[i]}")
            r_mult *= nums[j]
            print(f"r_mult is {r_mult} and nums[j] is {nums[j]}")
            
        return [l * r for l, r in zip(l_arr, r_arr)]