def max2(x,y):
    if x > y:
        return x
    else:
        return y

def max3(x,y,z):
    return max2(x,max2(y,z))

def max4(x,y,z,k):
    return max2(k,max3(x,y,z))

x = int(input())
y = int(input())
z = int(input())
k = int(input())

print(max4(x,y,z,k))
