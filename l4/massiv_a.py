A=[1,2,3,4,5]

for x in A:
    print(x, " - x from massive A[",x,"]", sep="")
    x+=x
    print(x, " - x*x from massive A[",int(x/2),"]", sep="")
print (A, type(A))


