#중복된 문자를 제외하고 사전에서 가장 먼저 찾을 수 있는 문자열

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 1.재귀
        for char in sorted(set(s)):
            #index()는 s에서 char이 처음으로 등장하는 인덱스를 반환
            suffix = s[s.index(char):]

            if set(s)==set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''

        # 2.스택
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            
            while stack and char < stack[-1] and counter[stack[-1]]>0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)


            






        