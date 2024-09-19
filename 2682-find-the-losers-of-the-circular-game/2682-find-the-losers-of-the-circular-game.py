class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # 플레이어 리스트 생성 (1부터 n까지)
        player = [i+1 for i in range(n)]
        
        # 공을 받은 플레이어들을 저장하는 리스트
        pick = []
        
        # 첫 번째 친구부터 공을 받기 시작
        current_position = 0
        cnt = 1
        
        # 첫 번째로 공을 받은 친구는 무조건 1번
        pick.append(player[current_position])

        while True:
            # cnt * k 만큼 시계 방향으로 이동
            next_position = (current_position + cnt * k) % n
            
            # 만약 다음 공을 받을 친구가 이미 공을 받은 친구라면 종료
            if player[next_position] in pick:
                break
            
            # 공을 받은 친구 리스트에 추가
            pick.append(player[next_position])
            
            # 현재 위치를 갱신하고, 공을 전달한 횟수를 증가
            current_position = next_position
            cnt += 1
        
        # 게임에서 한 번도 공을 받지 않은 친구들을 반환
        losers = [p for p in player if p not in pick]



        return losers