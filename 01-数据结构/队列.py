"""
    队列也是一种线性排列的数据结构，特点是先进先出。
        - 顺序队列，用数组实现的队列，有固定大小。
        - 链表队列，用链表实现的队列，没有固定大小。
"""


class Queue:
    """ 数组队列 """

    def __init__(self, size=1000):
        self.queue = [None for _ in range(size + 1)]  # None数组为底层数结构
        self.size = size + 1  # 队列大小，用一个额外空间判断队满或队空
        self.front = 0  # 指向队列元素的前一位
        self.rear = 0  # 指向最后一位队列元素

    def is_empty(self):
        """ 判断队列是否为空 """
        return self.front == self.rear

    def is_full(self):
        """ 判断队列是否为满 """
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        """ 将元素入队 """
        if self.is_full():
            raise Exception("Queue is full!")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    def dequeue(self):
        """ 将元素出队 """
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]

    def front_value(self):
        """ 获取队头元素 """
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            index = (self.front + 1) % self.size
            return self.queue[index]

    def rear_value(self):
        """ 获取队尾元素 """
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            index = (self.rear + 1) % self.size
            return self.queue[index]

    def show(self):
        """ 打印队列 """
        print("队头 ", end="")
        if self.front > self.rear:
            for n in range(self.front + 1, self.size):
                print("{} ".format(self.queue[n]), end="")
            for n in range(self.rear+1):
                print("{} ".format(self.queue[n]), end="")
        else:
            for n in range(self.front + 1, self.rear+1):
                print("<- {} ".format(self.queue[n]), end="")
        print()


class Node:
    """ 节点 """
    def __init__(self, value):
        self.value = value
        self.next = None


class linkListQueue:
    """ 链表队列 """
    def __init__(self):
        head = Node(0)
        self.front = head
        self.rear = head

    def is_empty(self):
        """ 判断队列是否为空 """
        return self.front == self.rear

    def enqueue(self, value):
        """ 将元素入队 """
        node = Node(value)
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        """ 将元素出队 """
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            node = self.front.next
            self.front.next = node.next
            if self.rear == node:
                self.rear = self.front
            value = node.value
            del node
            return value

    def front_value(self):
        """ 获取队头元素 """
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            return self.front.next.value

    def back_value(self):
        """ 获取队尾元素 """
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            return self.rear.value

    def show(self):
        """ 打印队列元素 """
        p = self.front.next
        print("队头", end="")
        while p:
            print(" <- {}".format(p.value), end="")
            p = p.next
        print()

if __name__ == '__main__':
    arrayQueue = Queue()
    linkListQueue = linkListQueue()
    colors = ["Red", "Blue", "Yellow", "Green"]
    for c in colors:
        arrayQueue.enqueue(c)
        linkListQueue.enqueue(c)

    arrayQueue.show()
    linkListQueue.show()
