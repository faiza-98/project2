#matrix in a list form
A=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print("the matrix is", A)
#initialize the result
result=[[0,0,0],[0,0,0],[0,0,0]]
#iterate with rows
for i in range(len(A)):
    for j in range(len(A[0])):  #iterate with columns
        result[j][i]=A[i][j]
print("the transpose is ")
for r in result:
    print(r)
    
