#q23 stack(LIFO)을 queue(FIFO)로 구현
'''
(생각할 점)
- dequeue에서 pop과 popleft
- queue의 peek, input stack의 요소들이 output stack에 역순으로 들어감
'''
class MyStack:

    def __init__(self):
        self.q = collections.deque()
        

    def push(self, x: int) -> None:
        #x를 앞으로 보내야 함, stack은 LIFO이므로
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        

    def pop(self) -> int:
        #popleft는 앞쪽에서 제거, push에서 x가 앞으로 가기 때문에 앞을 제거해야 함
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q) == 0
    

#q24 queue를 stack으로 구현
class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
        

    def push(self, x: int) -> None:
        self.input.append(x)
        

    def pop(self) -> int:
        #input stack의 요소들이 output stack에 역순으로 들어감
        self.peek()
        return self.output.pop()
        

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        

    def empty(self) -> bool:
        return self.input == [] and self.output == []