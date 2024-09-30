class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # 역방향 거리 = 전체 둘레 - 정방향 거리
        # 0, 1, 2, 3
        a = 0
        b = 0
        total = sum(distance)

        i = start

        while i != destination:
            a += distance[i]
            i = (i + 1) % len(distance)

        b = total - a
        return min(a, b)
        
        
        
        
        if start > destination:
            start, destination = destination, start
        a = 0
        b = 0
        total = sum(distance)
        a = sum(distance[start:destination])
        # a = (i + 1) % len(distance)
        
        b = total - a
        
        return min(a, b)