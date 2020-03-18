"""Norman Raphael M. Gaviola

DATALOG Lab01
Feb. 18, 2020
I have neither received nor provided any help on this (lab) activity, nor have I concealed any violation of the Honor Code."""

# importing the required module
import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1,20,10 )
plt.xlabel('log x')
plt.ylabel('log y')
plt.title("Plot of R-3.1\n DATALgo Feb. 19, 2020 \n i7@1.30GHz,Win10")
plt.xscale('log')
plt.yscale('log')
#n = 10
y1 = 8*n
y2 =  4*n*np.log(n)
y3 =2**n
y4 = n**3
y5 = 2 **n
plt.plot(n,y1,label = '8n')
plt.plot(n,y2,label ='4n log n')
plt.plot(n,y3,label ='2n^2')
plt.plot(n,y4,label ='n^3')
plt.plot(n,y5,label = ' 2^n')
plt.show()