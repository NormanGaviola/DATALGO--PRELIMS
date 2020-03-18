"""Norman Raphael M. Gaviola
   DATALOG Lab02 
   Feb.9,2020 
   I have neither received nor provided any help on this lab activity,nor have I concealed any violation of the Honor Code.
"""

def distinct(x): # to determine if the numbers are distinct
    y = set() #making empty list
    for z in x:
        if z in y: #identify if there same elements in list
          print(end ="")#print in a single line
          return False          
        y.add(z) #adds a given element that is not in the set
    print(end ="")
    return True


first_set_numbers = [1,1,2,2,3,3,4,4,5,5]
print(first_set_numbers,end=" ")
print(distinct(first_set_numbers))
second_set_numbers = [1,2,3,4,5,6,7,8,9,10]
print(second_set_numbers,end = " ")
print(distinct(second_set_numbers))