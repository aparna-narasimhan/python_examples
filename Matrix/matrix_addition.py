x=[[1,2,3],[4,5,6],[7,8,9]]

y=[[1,2,3],[4,5,6],[7,8,9]]

z=[[0,0,0,],[0,0,0],[0,0,0]]

for row in range(len(x)):
    
    for col in range(len(x[0])):

        z[row][col] = x[row][col]+y[row][col]


print(z)