class Solution:
    def repeatedCharacter(self, s: str) -> str:
        sdic = {}
        for c in s:
            if c not in sdic:
                sdic[c] = 0
            sdic[c] += 1
            if sdic[c] == 2:
                return c