"""
    链表数数据结构之一，其中的数据呈线性排列，特点是内存不连续。
        - 单链表，最基本的链表形式。
        - 循环链表，首尾相连，用来保存固定数量的数据。
        - 双向链表，节点有前驱指针和后继指针。
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
        return self.size == 0

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
        if self.is_empty():
            raise Exception("LinkList is empty!")
        else:
            tmp = self.head.next
            self.head.next = tmp.next
            self.size -= 1
            del tmp


if __name__ == '__main__':
    colorLinkList = linkList()
    colors = ["Red", "Blue", "Yellow", "Green"]
    # colorLinkList.pop()
    for t in colors:
        colorLinkList.push(t)
    colorLinkList.show_value()
