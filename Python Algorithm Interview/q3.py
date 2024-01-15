#로그 파일 재정렬
from typing import List


def reorderLogFiles(logs:List[str])->List[str]:
    letters, digits = [], []
    for log in logs:
        # log를 공백을 기준으로 나눈 두번째 부분
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    #람다 표현식? 
    #lambda는 파이썬의 익명 함수를 생성하는 키워드임
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters+digits


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(reorderLogFiles(logs))