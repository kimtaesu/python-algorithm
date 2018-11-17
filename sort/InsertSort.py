data = [15, 111, 1, 77, 3, 7, 8]


def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def insertSort(x):
    for i in range(1, len(x)):
        while 0 < i and x[i] < x[i - 1]:
            swap(x, i, i - 1)
            i -= 1
        print(x)
    return x


print(insertSort(data))


# [15, 111, 1, 77, 3, 7, 8]
# [1, 15, 111, 77, 3, 7, 8]
# [1, 15, 77, 111, 3, 7, 8]
# [1, 3, 15, 77, 111, 7, 8]
# [1, 3, 7, 15, 77, 111, 8]
# [1, 3, 7, 8, 15, 77, 111]
# [1, 3, 7, 8, 15, 77, 111]
