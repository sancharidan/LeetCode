class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_elems = len(nums)
        d = {}
        for i in range(0,num_elems):
            x = nums[i]
            y = target - x
            if y in d:
                return [d[y], i]
            else:
                d[x] = i