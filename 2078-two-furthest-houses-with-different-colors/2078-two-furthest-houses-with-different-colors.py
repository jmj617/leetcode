class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        distance = 0
        for i in range(len(colors)-1):
            for j in range(i+1, len(colors)):
                if colors[i] != colors[j]:
                    dif = j - i
                    distance = max(distance, dif)
        
        return distance