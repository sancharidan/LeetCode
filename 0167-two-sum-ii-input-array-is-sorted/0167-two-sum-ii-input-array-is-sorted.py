class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            complement = target - numbers[i]
            bs = self.binarySearch(numbers[i+1:],complement)
            
            if bs!=-1:
                return [i+1,bs+i+1+1]
            
    def binarySearch(self, nums: list[int], target: int) ->int:
        L = 0
        H = len(nums)-1
        while(L<=H):
            M = int((L+H)/2)
            if target == nums[M]:
                return M
            elif target < nums[M]:
                H = M-1
            elif target > nums[M]:
                L = M+1
        return -1