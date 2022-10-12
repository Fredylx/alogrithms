'''
Python 3
Fredy H Lopez
10/11/2022
Youtube: Algorithms and Data Structures Tutorial - Full Course for Beginners
'''
def linear_search(list, target):
    '''
    Returns the index position of the traget if found, else returns None
    '''
    
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")
        
numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 6)
verify(result)













