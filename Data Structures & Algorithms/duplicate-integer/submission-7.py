class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for v in Counter(nums).values():
            if v > 1:
                return True
        return False