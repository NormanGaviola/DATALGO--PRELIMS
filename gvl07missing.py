"""Norman Raphael M. Gaviola
   DATALOG Lab02
   March 18,2020
   I have neither received nor provided any help on this (lab) activity, nor have I concealed any violation of the Honor Code."""

def findFirstMissing(array, start, end):
    if (start > end):
        return end + 1

    if (start != array[start]):
        return start;

    mid = int((start + end) / 2)

    # Left half from 0 to mid
    if (array[mid] == mid):
        return findFirstMissing(array,
                                mid + 1, end)

    return findFirstMissing(array,
                            start, mid)


# driver program to test above function
arr1 = [0, 1, 2, 3, 6, 10, 11, 17]
arr2 = [1, 2, 3, 4, 6, 11, 17]
arr3 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr1)
n = len(arr2)
n = len(arr3)
print("Smallest missing in first set is",  #print the missing in set 1
      findFirstMissing(arr1, 0, n - 1))
print("Smallest missing in second set is", #print the missing in set 1
      findFirstMissing(arr2, 0, n - 1))
print("Smallest missing in third set is",  #print the missing in set 1
      findFirstMissing(arr3, 0, n - 1))