class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            c = target - nums[i]
            if c in seen:
                return [seen[c], i]
            else:
                seen[nums[i]] = i