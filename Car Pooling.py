class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        counts = [0 for _ in range(1001)] # 0 ~ 1000
        for num, f, t in trips:
            for i in range(f, t):
                counts[i] += num 
        return max(counts) <= capacity
