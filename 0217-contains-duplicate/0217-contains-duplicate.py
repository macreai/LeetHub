class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        saved_num = set()
        for num in nums:
            if num in saved_num:
                return True
            else:
                saved_num.add(num)
        return False
        