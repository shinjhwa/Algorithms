class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #각 문자가 마지막으로 등장한 위치를 기록
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used[char] = index

        return max_length
        
        
