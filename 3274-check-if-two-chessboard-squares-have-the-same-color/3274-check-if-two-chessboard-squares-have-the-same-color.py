class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # 알파벳 부분을 'a'를 1로 간주하여 숫자로 변환
        col1 = ord(coordinate1[0]) - ord('a') + 1
        col2 = ord(coordinate2[0]) - ord('a') + 1
        
        # 숫자 부분은 그대로 정수로 변환
        row1 = int(coordinate1[1])
        row2 = int(coordinate2[1])
        
        # 첫 번째 좌표의 색상 판별 (흑색인지 확인)
        color1_is_black = (col1 + row1) % 2 == 0
        
        # 두 번째 좌표의 색상 판별 (흑색인지 확인)
        color2_is_black = (col2 + row2) % 2 == 0
        
        # 두 좌표의 색상이 같으면 True 반환
        return color1_is_black == color2_is_black