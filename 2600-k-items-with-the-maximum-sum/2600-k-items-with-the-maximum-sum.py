class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        sum_num = 0
        one = [1] * numOnes
        zero = [0] * numZeros
        nega = [-1] * numNegOnes
        num_list = one + zero + nega
        for i in range(k):
            sum_num += num_list[i]
        return sum_num