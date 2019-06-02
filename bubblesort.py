def bubblesort(a):
    for passnum in range (len(a)-1,0,-1):
        for i in range (passnum):
            if a[i]>a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp

list = [10,34,45,60,22,12,28]
bubblesort(list)
print(list)
