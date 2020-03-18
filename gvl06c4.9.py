"""Norman Raphael M. Gaviola
   DATALOG Lab02
   March 4,2020
   I have neither received nor provided any help on this (lab) activity, nor have I concealed any violation of the Honor Code."""

def maximum(L): #to set the min and max
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0],maximum(L[1:]))
L= [2,4,6,23,56]   #inputs in min and max
print ("maximum is", maximum(L))  #prints the maximum