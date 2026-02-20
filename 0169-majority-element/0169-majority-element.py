class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        saved_data = {}
        for num in nums:
            saved_data[num] = saved_data.get(num, 0) + 1
        return max(saved_data, key=saved_data.get)
        