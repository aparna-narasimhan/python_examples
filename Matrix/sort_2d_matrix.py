#Approach 1: Sort 2D matrix in place
def sort_2d_matrix(A, m, n):
  t=0
  for x in range(m):
    for y in range(n):
      for i in range(m):
        for j in range(n):
          if(A[i][j]>A[x][y]):
            print("Swapping %d with %d"%(A[i][j], A[x][y]))
            t=A[x][y]
            A[x][y]=A[i][j]
            A[i][j]=t
  for i in range(m):
    print(A[i])

A = [[8,3,4],[2,1,6],[5,9,7]]
for i in range(3):
    print(A[i])
print("\n")
sort_2d_matrix(A, 3, 3)

#Approach 2: Saving the 2D Array into a 1D Array, sort the array and place it back in the 2D array
    int B[]=new int[m*n]; //creating a 1D Array of size 'r*c'
    int x = 0;
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            B[x] = A[i][j];
            x++;
        }
    }

    #Sorting the 1D Array in Ascending Order - Bubble sort

    int t=0;
    for(int i=0; i<(m*n)-1; i++)
    {
        for(int j=i+1; j<(m*n); j++)
        {
            if(B[i]>B[j])
            {
                t=B[i];
                B[i]=B[j];
                B[j]=t;
            }
        }
    }

    #Saving the sorted 1D Array back into the 2D Array

    x = 0;
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            A[i][j] = B[x];
            x++;
        }
    }