# 04. 가장 흔한 단어
# 금지한 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을
# 하지 않으며, 구두점(마침표, 쉼표) 또한 무시한다.
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]

# 풀이1. 리스트 컴프레션, counter객체 사용
# 1. 전처리
'''
words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
    .lower().split()
         if word not in banned]
'''
# 정규식 \w -> 단어 문자, ^ -> not

# 2. 단어 개수 세기
'''
counts = collections.defaultdict(int)
for word in words:
    counts[word] += 1
'''

# 3. 값이 가장 큰 key를 가져오기
''''
return max(counts, key=count.get)
'''

# 4. 가장 흔한 단어 추출
'''
counts = collections.Counter(words)
return counts.most_common(1)[0][0]
'''

# 결과
from typing import List

class Solution:
    def mostCommonWord(paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                    if word not in banned]
        counts = collections.Counter(words)
        # 가장 흔한 단어 첫째 인덱스 리턴
        return counts.most_common(1)[0][0]

mostCommonWord(paragraph='Bob hit a ball, the hit BALL flew far after it was hit',
               banned=["hit"])