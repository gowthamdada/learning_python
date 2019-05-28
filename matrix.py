R = int(input("enter the number of rows:"))
C = int(input("enter the number of rows:"))

matrix = []
print("enter the entries row_wise")

#getting an input

for i in range (R):
    a = []
    for j in range (C):
        a.append(int(input()))
    matrix.append(a)

#to print the matrix

for i in range (R):
    for j in range (C):
        print(matrix[i][j])
    print()
