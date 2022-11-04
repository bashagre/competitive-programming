class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        output = 0

        nums.sort()

        small, big = 0, len(nums)-1

        while small < big:

            if nums[small] + nums[big] == k:
                #print("found pair")
                output += 1
                small += 1
                big -= 1

            elif nums[small] + nums[big] < k:
                #print("less")
                small += 1
            elif nums[small] + nums[big] > k:
                #print("greater")
                big -= 1
        return output
        
        
                    
