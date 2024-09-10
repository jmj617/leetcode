class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        children = [i for i in range(n)]
        a = 2 * (n - 1)
        print(children)
        if n < (k % a):
            answer = children[-2 -((k % a) - n)]
        else:
            answer = k % (2 * (n - 1))


        return answer
