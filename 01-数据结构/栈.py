"""
    栈是一种数据呈线性排列的数据结构，但只能访问最新添加的数据，特点是先进先出。
        - 数组栈，通过数组实现，有固定大小。
        - 链表栈，通过链表实现，没有固定大小。
"""


class Stack:
    """ 数组栈 """
    def __init__(self, size=1000):
        self.stack = []  # 数组作为底层结构
        self.size = size  # 栈的大小
        self.index = -1  # 栈顶位置

    def is_empty(self):
        """ 判断栈是否为空 """
        return self.index == -1

    def is_full(self):
        """ 判断栈是否满 """
        return self.index == self.size - 1

    def push(self, value):
        """ 将元素入栈 """
        if self.is_full():
            raise Exception("Stack is full!")
        else:
            self.stack.append(value)
            self.index += 1

    def pop(self):
        """ 将元素出栈 """
        if self.is_empty():
            raise Exception("Stack is empty!")
        else:
            self.stack.pop()
            self.index -= 1

    def top(self):
        """ 获得栈顶元素 """
        if self.is_empty():
            raise Exception("Stack is empty!")
        else:
            return self.stack[self.index]

    def show(self):
        """ 打印栈内的元素 """
        print("栈底 | ", end="")
        print(" | ".join(self.stack))


class Node:
    """ 节点 """
    def __init__(self, value):
        self.value = value
        self.next = None


class linkListStack:
    """ 链表栈 """
    def __init__(self):
        self.head = Node(0)     # 头节点
        self.size = 0       # 栈长度

    def is_empty(self):
        """ 判断栈是否为空 """
        return self.size == 0

    def push(self, value):
        """ 将元素入栈 """
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        """ 将元素出栈 """
        if self.is_empty():
            raise Exception("Stack is empty!")
        else:
            node = self.head.next
            self.head.next = node.next
            del node
            self.size -= 1

    def top(self):
        """ 获得栈顶元素 """
        if self.is_empty():
            raise Exception("Stack is empty!")
        else:
            return self.head.next.value

    def show(self):
        """ 打印链表 """
        node = self.head.next
        while node:
            print("{} | ".format(node.value), end="")
            node = node.next
        print("栈底")


if __name__ == '__main__':
    colors = ["Red", "Blue", "Yellow", "Green"]

    arrayStack = Stack()
    linkListStack = linkListStack()
    for c in colors:
        linkListStack.push(c)
        arrayStack.push(c)
    print("数组栈：")
    arrayStack.show()
    print("链表栈：")
    linkListStack.show()
