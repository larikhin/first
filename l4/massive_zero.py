A=[0]*1000
top = 0
print("input x ", end="")
x = int(input())
while x!=0:
    A[top]=x
    top+=1
    print('input element in massive ')
    x =int(input())
for k in range(4,-1,-1):
    print(A[k])
print(A)

