# Author: @CodeWithSalman

# IMPORTING ARRAY FROM ARRAY MODULE.
# HERE arr IS CALLED ALIAS.
import array as arr
# GOING TO USE INTEGER ARRAY.
array_Data = arr.array('i', [44, 22, 44, 66])
# FIRST OF ALL LET'S SORT THIS ARRAY.
sorted_Array = sorted(array_Data)
# CHECKING RESULT.
print("Array Before: ")
for i in sorted_Array:
    print(i, end=" ")
# NOW LET'S REMOVE DUPLICATIONS.
removing_Duplications = arr.array('i')
print("\nArray after removing duplications")
for i in sorted_Array:
    if i not in removing_Duplications:
        removing_Duplications.append(i)
        print(i, end=" ")
