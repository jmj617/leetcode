class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # col1 = ord(coordinate1[0]) - ord('a') + 1
        # col2 = ord(coordinate2[0]) - ord('a') + 1
        
        # row1 = int(coordinate1[1])
        # row2 = int(coordinate2[1])
        
        # color1_is_black = (col1 + row1) % 2 == 0
        
        # color2_is_black = (col2 + row2) % 2 == 0
        
        # # 두 좌표의 색상이 같으면 True 반환
        # return color1_is_black == color2_is_black

        black = ['a', 'c', 'e', 'g']
        if (coordinate1[0] in black) == (coordinate2[0] in black):
            # 시작 색 같을 때
            if (int(coordinate1[1]) % 2) == (int(coordinate2[1]) % 2):
                return True
            else:
                return False
        else:
            if (int(coordinate1[1]) % 2) != (int(coordinate2[1]) % 2):
                return True
            else:
                return False