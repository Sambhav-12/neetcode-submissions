class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = 1
        for ltr in range(len(nums)):
            result.append(prefix)
            prefix *= nums[ltr]
        
        suffix = 1
        for rtl in range(len(nums) - 1, -1 , -1):
            result[rtl] *= suffix
            suffix *= nums[rtl]

        return result
