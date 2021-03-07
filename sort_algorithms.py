def selection_sort(items):
    for i in range(0, len(items) - 1):
        minimum = i
        for j in range(i, len(items)):
            if items[minimum] > items[j]:
                minimum = j
        items[i], items[minimum] = items[minimum], items[i]


def insertion_sort(items):
    for i in range(1, len(items)):
        for j in range(i, 0, -1):
            if items[j - 1] > items[j]:
                items[j], items[j - 1] = items[j - 1], items[j]
            else:
                break


def shell_sort(items):
    h = len(items) // 2
    while h >= 1:
        for i in range(h, len(items)):
            j = i
            while j >= h and items[j] < items[j - h]:
                items[j], items[j - h] = items[j - h], items[j]
                j -= h
        # print(f"{h}-sort result: ", items)
        h //= 2


def downheap(i, size):
    while 2 * i + 1 <= size:
        k = 2 * i + 1
        if k < size - 1 and items[k] < items[k + 1]:
            k += 1
        if items[i] >= items[k]:
            break
        items[i], items[k] = items[k], items[i]
        i = k


def heapify(items):
    hsize = len(items)
    for i in range(hsize // 2 - 1, -1, -1):
        downheap(i, hsize)


def heap_sort(items):
    N = len(items)
    for i in range(N):
        items[0], items[N - 1] = items[N - 1], items[0]
        downheap(0, N - 2)
        N -= 1

def merge(items, temp, low, mid, high):
    i = low
    j = mid + 1
    for k in range(low, high + 1):
        if i > mid:
            temp[k] = items[j]
            j += 1
        elif j > high:
            temp[k] = items[i]
            i += 1
        elif items[j] < items[i]:
            temp[k] = items[j]
            j += 1
        else:
            temp[k] = items[i]
            i += 1
    for k in range(low, high + 1):
        items[k] = temp[k]


def merge_sort(items, temp, low, high):
    if high <= low:
        return None
    mid = low + (high - low) // 2
    merge_sort(items, temp, low, mid)
    merge_sort(items, temp, mid + 1, high)
    merge(items, temp, low, mid, high)


def partition(items, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and items[i] < items[pivot]:
            i += 1
        while j > pivot and items[j] > items[pivot]:
            j -= 1
        if j <= i:
            break
        items[i], items[j] = items[j], items[i]
        i += 1
        j -= 1
    items[pivot], items[j] = items[j], items[pivot]
    return j


def quik_sort(items, low, high):
    if low < high:
        pivot = partition(items, low, high)
        quik_sort(items, low, pivot - 1)
        quik_sort(items, pivot + 1, high)
