data = [15, 111, 1, 77, 3, 7, 8]


def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def selectionSort(x):
    for i in range(0, len(x) - 1):
        max = i
        for j in range(i + 1, len(x)):
            if x[j] < x[max]:
                max = j
        swap(x, max, i)
    return x


print(selectionSort(data))
