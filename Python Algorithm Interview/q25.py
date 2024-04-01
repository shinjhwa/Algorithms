#Design Circular Queue
'''
(생각할 점)
-front=0, rear=0 or front=0, rear=-1인 경우
'''
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None]*k
        self.front = 0  
        self.rear = 0 #enQueue를 하면 rear는 요소가 들어갈 다음 인덱스를 가리킴
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear+1)%self.size
        return True

        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front] = None #선택사항
        self.front = (self.front+1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        last_elem_index = (self.rear - 1 + self.size) % self.size
        return self.queue[last_elem_index]
        

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is None
        

    def isFull(self) -> bool:
        #rear가 넣을 곳의 인덱스라서 isEmpty와 isFull 모두 front와 queue가 같은 상황임
        return self.front == self.rear and self.queue[self.front] is not None