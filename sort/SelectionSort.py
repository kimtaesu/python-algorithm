data = [15, 111, 1, 77, 3, 7, 8]


def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def selectionSort(x):
    for i in range(0, len(x) - 1):
        min = i
        for j in range(i + 1, len(x)):
            if x[j] < x[min]:
                min = j
        swap(x, min, i)
        print("{} {}".format(x, min))
    return x


print(selectionSort(data))

# [1, 111, 15, 77, 3, 7, 8] 2
# [1, 3, 15, 77, 111, 7, 8] 4
# [1, 3, 7, 77, 111, 15, 8] 5
# [1, 3, 7, 8, 111, 15, 77] 6
# [1, 3, 7, 8, 15, 111, 77] 5
# [1, 3, 7, 8, 15, 77, 111] 6
# [1, 3, 7, 8, 15, 77, 111]