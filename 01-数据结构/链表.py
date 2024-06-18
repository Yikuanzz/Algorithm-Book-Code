"""
    链表数数据结构之一，其中的数据呈线性排列。
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class linkList:
    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def is_empty(self):
        return True if self.size == 0 else False

    def show_value(self):
        if not self.is_empty():
            node = self.head.next
            while node:
                print("{} -> ".format(node.value), end="")
                node = node.next
            print("None")

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if not self.is_empty():
            tmp = self.head.next
            self.head.next = tmp.next
            self.size -= 1
            del tmp


if __name__ == '__main__':
    colorLinkList = linkList()
    colors = ["Red", "Blue", "Yellow", "Green"]
    for t in colors:
        colorLinkList.push(t)
    colorLinkList.show_value()
