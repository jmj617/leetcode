class Solution:
    def minimumChairs(self, s: str) -> int:
        chair = 0
        max_chair = 0
        for c in s:
            if c == 'E':
                chair += 1
            elif c == 'L':
                chair -= 1
            max_chair = max(chair, max_chair)
        return max_chair