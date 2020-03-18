"""Norman Raphael M. Gaviola
   DATALOG Lab02
   March 4,2020
   I have neither received nor provided any help on this (lab) activity, nor have I concealed any violation of the Honor Code."""

m = int(input("Value for m: "))
n = int(input("Value for n: "))
def multiply(m, n):# 0 multiplied with anything
    if (n == 0):
        return 0

    # Add x one by one
    if (n > 0):
        return (m + multiply(m, n - 1))

        # The case where y is negative
    if (n < 0):
        return -multiply(m, -n)

print("answer is", multiply(m, n))