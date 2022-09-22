#Solve the following question and create test cases with unittest

# Given an array nums, write a function to move all zeroes to the end of it 
# while maintaining the relative order of
# the non-zero elements.
#array1 = [0, 1, 0, 3, 12]
# Output:
# [1, 3, 12, 0, 0]

#array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]
# Output:
# [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]
array1 = [0, 1, 0, 3, 12]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]

def nozlist(a_list):
    nozeros = []
    for num in a_list:
        if num > 0:
            nozeros.append(num)
    return nozeros
nozlist(array1)
nozlist(array2)

def zlist(a_list):
    zeros = []
    for num in a_list:
        if num == 0:
            zeros.append(num)
    return zeros
zlist(array1)
zlist(array2)

def comp_list(a_list): #to make a function that joins two outputs(lists) still use a_list
    full_list = nozlist(a_list)+zlist(a_list)
    return full_list
print(comp_list(array1))
print(comp_list(array2))

        




