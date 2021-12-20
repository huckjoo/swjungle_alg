class MyCircularDeque:

    def __init__(self, k: int):
        self.count = 0
        self.rear = 0
        self.front = k-1
        self.buffer = [0]*k
        self.size = k

    def insertFront(self, value: int) -> bool:
        if self.isFull() == False:
            self.buffer[self.front] = value
            self.front = (self.front-1) % self.size
            self.count += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.isFull() == False:
            self.buffer[self.rear] = value
            self.rear = (self.rear+1) % self.size
            self.count += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.isEmpty() == False:
            self.front = (self.front+1) % self.size
            self.count -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.isEmpty() == False:
            self.rear = (self.rear-1) % self.size
            self.count -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.isEmpty() == False:
            return self.buffer[(self.front+1) % self.size]
        else:
            return -1

    def getRear(self) -> int:
        if self.isEmpty() == False:
            return self.buffer[(self.rear-1) % self.size]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.count == self.size:
            return True
        else:
            return False
