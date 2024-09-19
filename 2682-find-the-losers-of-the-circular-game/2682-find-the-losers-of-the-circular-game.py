class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        player = [i+1 for i in range(n)]

        pick = []
        pick.append(player[0])

        now = 0
        cnt = 1
        while True:

            next_po = (current_position + cnt * k) % n

            if player[next_po] in pick:
                break
            
            pick.append(player[next_po])

            now = next_po
            cnt += 1

        answer = [i for i in player if i not in pick]



        return answer