# 03. 로그 파일 재정렬
# 로그를 재정렬하라. 기준은 다음과 같다.
# 1.로그의 가장 앞 부분은 식별자다.
# 2.문자로 구성된 로그가 숫자 로그보다 앞에 온다
# 3.식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 4.숫자 로그는 입력 순서대로 한다.

logs = ['dig1 8 1 5 1', 'let1 art can','dig2 3 6','let2 own kit dig','let3 art zero']

# 풀이1. 람다와 +연산자를 이용
# 1. split()과 isdigit()를 이용해서 두번째가 숫자인지 확인
'''
if log.split()[1].isdigit():
    digits.append(log)
else:
    letters.append(log)
'''

# 2. digits와 letters로 모인 문자 로그를 정렬
'''
letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
'''
# 식별자를 제외한 문자열[1:]을 키로하여 정렬 하고
# 후순위 식별자 [0]를 지정해 정렬되도록 함

# 3. 두 문자열 digits와 letters를 합친다

# 결과
from typing import List

class Solution:
    def reorderLogFiles(logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        # 2개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits

reorderLogFiles(logs)