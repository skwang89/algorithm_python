# 02. 문자열 뒤집기
# 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며,
# 리턴 없이 내부를 직접 조작하라.

# 풀이 1. 투 포인터를 이용한 스왑
from typing import List

class Solution:
    def reverseString(s: List[str]) -> None:
        left, right = 0, len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

a = ['h','e','l','l','o']
b = ['H','a','n','n','a','h']
reverseString(a)
reverseString(b)
a
b

# 풀이 2. 파이썬 다운 방식
from typing import List

class Solution:
    def reverseString(s: List[str]) -> None:
        s.reverse()

a = ['h','e','l','l','o']
b = ['H','a','n','n','a','h']
reverseString(a)
reverseString(b)
a
b