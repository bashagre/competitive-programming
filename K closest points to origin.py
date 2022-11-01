class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        points.sort(key=lambda nums: nums[0]**2 + nums[1]**2 )
        return (points[:k])
     
