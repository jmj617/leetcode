class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # 역방향 거리 = 전체 둘레 - 정방향 거리

        a = 0
        b = 0
        total = sum(distance)
        for i in range(len(distance)):
            if i + 1 == destination:
                a = sum(distance[:i+1])
                # a = (i + 1) % len(distance)
                b = total - a
        
        return min(a, b)