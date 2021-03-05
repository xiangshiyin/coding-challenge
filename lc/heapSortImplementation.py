
def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return (i + 1) // 2 - 1

def max_heapify(A, i):
    l = left(i)
    r = right(i)

    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < len(A) and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i] # swap
        max_heapify(A, largest)
        

def build_max_heap(A):
    i = len(A) // 2 - 1
    while i >= 0:
        max_heapify(A, i)
        i -= 1


def heap_sort(A):
    result = []
    # build a max heap
    build_max_heap(A)
    # traverse the list and do heap sort
    while len(A) > 1:
        result.append(A[0])
        A[0],A[len(A)-1] = A[len(A)-1],A[0]
        A.pop() # could also set a limit to max_heapify range in order to do in-place sort
        max_heapify(A, 0)
    result.extend(A)
    return result




if __name__ == '__main__':
    A=[1,2,3,4,5,7,8,10,400]
    result = heap_sort(A)
    print(result)

