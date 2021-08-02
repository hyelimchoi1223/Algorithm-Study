class Solution:
    def twoSum(self, nums, target):
        for idx_x, i in enumerate(nums[:-1]):
            for idx_y, j in enumerate(nums[idx_x+1:], idx_x+1):
                if i+j == target:
                    return [idx_x, idx_y]
