class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        leftSum = 0
        rightSum = sum(nums)

        

        for i in range(len(nums)):

            rightSum -= nums[i]

            if leftSum == rightSum:
                #print(i)
                return i
            leftSum += nums[i]
        #print("-1")
        return -1
        
            
        
            
