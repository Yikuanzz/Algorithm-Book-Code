class queue():
    def __init__(self, size=1000):
        """ 约定 self.front 指向队列头的前一个元素 self.rear 指向队列的最后一个元素"""
        self.size = size
        self.queue = [None for _ in range(size + 1)]
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Queue is full!")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]

    def front_value(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            index = (self.front + 1) % self.size
            return self.queue[index]

    def back_value(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            index = (self.rear + 1) % self.size
            return self.queue[index]

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkListQueue:
    def __init__(self):
        head = Node(0)
        self.front = head
        self.rear = head

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self, value):
        node = Node(value)
        node.next = self.rear.next
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            node = self.front.next
            self.front = node.next
            if node == self.rear:
                self.rear = self.front
            value = node.value
            del node
            return value

    def front_value(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            return self.front.next.value

    def back_value(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            return self.rear.value

