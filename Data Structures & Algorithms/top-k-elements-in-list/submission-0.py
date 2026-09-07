class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in count:
            buckets[count[num]].append(num)
        result = []
        for i in range(len(nums) , 0 , -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
                    break