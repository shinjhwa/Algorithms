#가장 흔한 단어
from typing import List
import re
import collections


def mostCommonWord(paragraph: str, banned: List[str])->str:
    words = [word for word in re.sub(r'[^\w]', " ", paragraph).lower().split() if word not in banned]
    #Counter객체 이용
    counts = collections.Counter(words)

    return counts.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit Ball flew far after it was hit"
banned = ["hit"]
        

print(mostCommonWord(paragraph, banned))