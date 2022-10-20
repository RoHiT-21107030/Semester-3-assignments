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
# An in-place Python program
# to reverse an array

''' Function to reverse arr[]
	from start to end'''
def reverseArray(arr, n):
	
	for i in range(0, int(n / 2)):
		arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]


# Driver code
if __name__ == "__main__":
	
	arr = [1, 2, 3, 4, 5, 6]
	n = len(arr)
	print(*arr)
	reverseArray(arr, n)
	print("Reversed array is")
	print(*arr)
	
# An Not in-place Python program
# to reverse an array

''' Function to reverse arr[]
	from start to end '''
def reverseArray(arr, n):
	
	# Create a copy array
	# and store reversed
	# elements
	rev = n * [0]
	for i in range(0, n):
		rev[n - i - 1] = arr[i]
			
	# Now copy reversed
	# elements back to arr[]
	for i in range(0, n):
		arr[i] = rev[i]
		
# Driver code
if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5, 6]
	n = len(arr)
	print(*arr)
	reverseArray(arr, n);
	print("Reversed array is")
	print(*arr)
	

"""
Q3. Suggest some practical examples of using in-place and out-place techniques.
 
A3. In Place: Bubble sort, Selection Sort, Insertion Sort, Heapsort. 
    QuickSort uses extra space for recursive function calls. It is called in-place
    according to broad definition as extra space required is not used to manipulate input, but only for recursive calls.
    
    Not In-Place: Merge Sort. Note that merge sort requires O(n) extra space.
"""

   
