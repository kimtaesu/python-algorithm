data = [15, 111, 1, 77, 3, 7, 8]


def swap(x, i, j):
    x[i], x[j] = x[j], x[i]


def mergeSort(list):
    if len(list) > 1:
        mid = len(list) // 2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k] = lefthalf[i]
                i += 1
            else:
                list[k] = righthalf[j]
                j += 1
            k = k + 1

        while i < len(lefthalf):
            list[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            list[k] = righthalf[j]
            j += 1
            k += 1


mergeSort(data)

print(data)
