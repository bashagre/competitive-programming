class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        leftProduct = [0]*size
        rightProduct = [0]*size
        leftProduct[0] = 1
        rightProduct[size-1] = 1
        
        for i in range(1,size):
            leftProduct[i] = leftProduct[i-1] * nums[i-1]
            rightProduct[size-i-1] = rightProduct[size-i] * nums[size-i]
        
        ans = []
        for i in range(size):
            ans.append(leftProduct[i] * rightProduct[i])
        return ans
