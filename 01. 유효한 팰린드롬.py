# 01. 유효한 팰린드롬
# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며,
# 영문자와 소문자만을 대상으로 한다.
# "A man, a plan, a canal: Panama" -> True
# "race a car"  -> False

# 풀이 1. 리스트로 변환
# 1. 전처리: 대소문자 구분 x, 영문자 숫자 만을 대상으로 함
'''
strs = []
for char in s:
    if char.isalnum():      # isalnum(): 영어와 숫자를 판별하는 함수
        strs.append(char.lower())
'''
# 2. 팰린드롬 여부 판별
'''
while len(strs) > 1:
    if strs.pop(0) !=strs.pop():
        return False
'''
# 결과
class Solution:
    def isPalindrome(s: str) -> bool:
        # 1. 전처리
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        # 2. 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

    a = 'A man, a plan, a canal: Panama'
    b = "race a car"
    type(a)
    type(isPalindrome(a))
    print(isPalindrome(a))

# 풀이 2. 데크 자료형을 이용한 최적화
import collections

class Solution:
    def isPalindrome(s: str) -> bool:
        # 자료형 데크로 선언
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

# 풀이 3. 슬라이싱 사용
import re

class Solution:
    def isPalindrome(s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]









