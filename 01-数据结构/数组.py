"""
    数组是数据呈线性排列的一种数据结构，特点是内存连续。

"""

if __name__ == '__main__':
    arr = []
    colors = ["Red", "Blue", "Yellow", "Green"]

    for c in colors:
        arr.append(c)

    print(" - ".join(arr))
