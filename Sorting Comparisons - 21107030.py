# Selection sort in Python


def selectionSort(array, size):
    swaps = 0
    comparisons = 0
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            comparisons += 1

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
                swaps += 1


        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
        swaps +=1
    print("Number of swaps:",swaps)
    print("Number of comparisons:", comparisons)


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)


# Bubble sort in Python

def bubbleSort(array):
    comparisons = 0
    swaps = 0
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):
            comparisons +=1

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swaps +=1
    print("Number of swaps:", swaps)
    print("Number of comparisons:", comparisons)


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)
