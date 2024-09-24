class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = [x for x in nums if x % 2 == 0]

        if not even:
            return -1
        
        maxi = 0
        answer = -1
        counter = Counter(even) 
        for n, c in counter.items():
            if c > maxi:
                maxi = c
                answer = n
            elif c == maxi:
                answer = min(n, answer)
        
        return answer