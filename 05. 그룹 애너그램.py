# 05. 그룹 애너그램
# 문자열을 받아 애너그램 단위로 그룹핑하라.
['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# 풀이1. 정렬하여 딕셔너리에 추가
# 1. sorted(): 문자열 정리후 리스트로 리턴
# 주의: sort()는 리스트 자체를 정렬하며 None을 리턴함
# 다시 키로 사용하기 위해 join()으로 합치기
# 애너그램 끼리는 같은 키를 갖게 됨
# 같운 키를 갖는 단어를 append()로 함침
'''
anagrams[''.join(sorted(word))].append(word)
'''

# 2. 정렬한 값을 키로 하여 딕셔너리에 추가.
# KeyError를 방지하지 위해 defaultdict()으로 선언
'''
anagrams = collentions.defaultdict(list)
'''

# 결과
from typing import List
import collections


class Soultion:
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()


a = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
groupAnagrams(a)

# 06. 가장 긴 팰린드롬 부분 문자열
# 가장 긴 팬린드롬 부분 문자열을 출력하라.
a = 'babad'
b = 'cbbd'
c = 'kdhfiwhkjdfdjhfdkhsskehfshfsk'

# 풀이1. 중앙을 중심으로 확장하는 풀이
# 파이썬 문자열 슬라이싱 이용
'''
if len(s) < 2 or s == s[::-1]:
    return s
'''

# 슬라이딩 윈도우가 문자열 처음부터 끝까지 우측으로 이동
'''
for i range(0, len(s) -1):
    result = max(result,
                 expand(s, i, i + 1),
                 expand(s, i, i + 2),
                 key=len)
    return result
'''


# 결과
class Solution:
    def longestPalindrome(s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1: right - 1]

        # 해당 사항이 없으면 리턴
        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result


longestPalindrome(a)
longestPalindrome(b)
longestPalindrome(c)