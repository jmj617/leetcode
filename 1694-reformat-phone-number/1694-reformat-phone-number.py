class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '')
        number = number.replace('-', '')
        cnt = len(number)
        answer = []
        i = 0
        while cnt > 4:
            answer.append(number[i:i + 3])
            i += 3
            cnt -= 3

        # 남은 숫자가 4자리인 경우 2-2로 나누기
        if cnt == 4:
            answer.append(number[i:i + 2])
            answer.append(number[i + 2:])
        else:  # 남은 숫자가 4보다 작거나 같으면 그대로 추가
            answer.append(number[i:])

        return '-'.join(answer)
                
            