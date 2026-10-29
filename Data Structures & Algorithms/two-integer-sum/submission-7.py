class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_h = {}
        for i, n in enumerate(nums):
            nums_h[n] = i
        for i in range(0, len(nums)):
            rest = target - nums[i]
            if rest in nums_h and nums_h[rest] != i:
                return [min(i, nums_h[rest]),  max(i, nums_h[rest])]
        return []
        