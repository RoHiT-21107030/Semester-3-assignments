"""
Q1. What is the difference between in-place and out-place sorting algorithms?
A1. An in-place algorithm is an algorithm that does not need an extra space 
    and produces an output in the same memory that contains the data by transforming 
    the input ‘in-place’. However, a small constant extra space used for variables is allowed.
    
    Out-place sorting is a class of sorting algorithms that can handle massive amounts of data. 
    Out-place sorting is required when the data being sorted do not fit into the main memory of a 
    computing device (usually RAM) and instead they must reside in the slower external memory, usually a disk drive.
"""

"""
Q2. Implement Insertion sort in both (in-place and out-place) manner.
"""
# Insertion sort in in-place manner.


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)



"""
Q3. Suggest some practical examples of using in-place and out-place techniques.
 
A3. In Place: Bubble sort, Selection Sort, Insertion Sort, Heapsort. 
    QuickSort uses extra space for recursive function calls. It is called in-place
    according to broad definition as extra space required is not used to manipulate input, but only for recursive calls.
    
    Not In-Place: Merge Sort. Note that merge sort requires O(n) extra space.
"""

   
