'''
Runtime: 72 ms, faster than 52.89% of Python3 online submissions for Design Circular Queue.
Memory Usage: 14.9 MB, less than 62.42% of Python3 online submissions for Design Circular Queue.
'''

'''
준영: % 연산자 써서 circular을 구현한 게 참신합니다. 
front랑 rear랑 같을 때가 queue가 빈 상태이고, rear가 front랑 떨어져 있을 떄, front(exclusive)에서 rear까지 만큼을 채워져 있는 queue라고 보신 점이 흥미롭습니다. 
다만, front 요소를 확인하려고 할 때 front에 1을 더한 곳에서 front element를 찾을 수 있었던 점은 직관과 다소 괴리가 있어 이해하는 게 어려웠습니다.
'''


class MyCircularQueue:

    def __init__(self, k: int):
        self.length = k+1
        self.arr = [None]*(k+1)
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        # 들어갈 수 없으면
        if((self.rear+1) % self.length == self.front % self.length):
            return False
        else:  # 들어갈 수 있으면
            self.arr[(self.rear+1) % self.length] = value
            self.rear = self.rear + 1
            return True

    def deQueue(self) -> bool:
        if(self.rear == self.front):  # 큐에 아무것도 없을 때는 뺄 수 없음
            return False
        else:  # 그게 아니라면 항상 뺄 수 있음
            self.arr[(self.front + 1) % self.length] = None
            self.front = self.front + 1
            return True

    def Front(self) -> int:
        if self.isEmpty() == True:
            return -1
        else:
            return self.arr[(self.front+1) % self.length]

    def Rear(self) -> int:
        if self.isEmpty() == True:
            return -1
        else:
            return self.arr[self.rear % self.length]

    def isEmpty(self) -> bool:
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if (self.rear+1) % self.length == self.front % self.length:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
