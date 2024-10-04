class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        taxes = 0
        prev_upper= 0

        for upper, percent in brackets:
            curr = min(income, upper - prev_upper)
            taxes += curr * (percent/100)
            income -= curr
            prev_upper = upper

            if income == 0:
                break
                
        return taxes