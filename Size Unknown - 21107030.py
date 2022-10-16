#importing array
import array as arr
#creatinh an array
a = arr.array('i', [1,2,4,5,3,7,35,7,34,25,6] )

# creating a function to find the size of the array
def size(list):
    length = 0
    for i in list:
        length+=1
    return length

# creating a function to find the position of the element in the array
def position(list, element):
    pos = 0
    for i in list:
        if i != element:
            pos+=1
        else:
            return pos

#creating a function to implement binary search
def binary_search(list, element):
    high = size(list)
    middle = size(list)//2
    required_list = []
    
    if middle > element:
        required_list = list[0: middle]

    elif middle< element:
        required_list = list[middle: high]

    elif middle == element:
        return middle
    for i in required_list:
        if i == element:
            return position(list, i) + 1
        else:
            return "Does not exist"


#checking the code
print(binary_search(a, 7))





