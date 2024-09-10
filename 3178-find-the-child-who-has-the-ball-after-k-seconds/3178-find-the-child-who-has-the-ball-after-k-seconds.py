class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        children = [i for i in range(n)]
        a = 2 * (n - 1)
        if n <= (k % a):
            answer = children[-2 -(k % a - n)]
        else:
            answer = k % a
        return answer

        # children = [i for i in range(n)]
        # queue = children + children[1:-1][::-1]
        # x = k % len(queue)
        # return queue[x]


