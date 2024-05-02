class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #해시 테이블
        freqs = {}

        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
        
        cnt = 0
        for char in jewels:
            if char in stones:
                cnt += freqs[char]

        return cnt   

        '''
        #Counter 사용
        freqs = collections.Counter(stones)
        cnt = 0
        for char in jewels:
            cnt += freqs[char]
        return cnt     
        '''
        
        '''
        #파이썬다운 방식
        return sum(s in J for s in S)
        '''
