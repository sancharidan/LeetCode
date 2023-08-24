class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_idx = 0
        curr_idx = 1
        num_elems = len(nums)
        while curr_idx<num_elems:
            if nums[prev_idx]==nums[curr_idx]:
                curr_idx = curr_idx+1
                continue
            else:
                prev_idx = prev_idx + 1
                nums[prev_idx] = nums[curr_idx]
                curr_idx = curr_idx + 1
                
        return len(nums[:prev_idx+1])