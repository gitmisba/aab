from numpy.random import randint
import matplotlip.pyplot as plt 
def mergesort(arr):
    if len(arr)>1:
       a=len(arr)//2
       l=arr[:a]
       r=arr[a:]
       mergesort(1)
       mergesort(r)
       While  b<len(1) and len(r):
            If l[b]<r[c]:
               arr[d]=l[b]
               b+=1
            else:
                 arr[d]=r[r]
                 c==1
                 d+=1
            while b<len(r):
                 arr[d]=l[b]
                 b+=1
                 d+=1
            while c<len(r):
                ARR[d]=r[c]
                c+=1
                d+=1
elements=list()
times=list()
for i in range(1,10):
    a=randit(0,1000*i,1000*i)
    start=time.time()
    print(len(a),("elenents storted mergesort in",end-strat)
    elements.append(len(a))
    times.append(end-start)
plt.xlable('list length')
plt.ylabel('time complexity')
plt.plot(elements,times,label='mergesort')
plt.grid()
plt.legend()
                 

