class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        for i in range(len(nums)):
            nums[i] = int(nums[i])

        nums.sort(reverse = True)
        #print(nums)
        output = str(nums[k-1])
        #print(type(output))
        #print(output)
        return output  
