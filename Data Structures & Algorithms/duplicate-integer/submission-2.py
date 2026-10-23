class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_aux = set()
        for num in nums:
            if not num in num_aux:
                num_aux.add(num)
            else:
                return True
        return False
        