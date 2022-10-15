'''
Python 3
Fredy H Lopez
10/11/2022
Youtube: Algorithms and Data Structures Tutorial - Full Course for Beginners
Linear binary search has a smaller time and space complexity. Usually.
'''

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
            
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)
            
def verify(result):
    print("target found: ", result)
    
numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)

            
        
