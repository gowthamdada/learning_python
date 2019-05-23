def bigger(a,b):
    if(a>b):
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

print("biggest number", biggest(2,3,4))
print ("bigger number", bigger(5,6))
