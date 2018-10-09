original=[
         [1,2,3],
         [6,7,6],
         [3,2,1]
       ]

#print(original)
transpose = zip(*original)
print(transpose)
last_to_first = zip(original[::-1]) #last to first
print(last_to_first)
rotated = zip(*original[::-1]) #rotates 90 degrees
print(rotated)
rotated_180_deg = zip(*rotated[::-1])
print(rotated_180_deg)

def transpose():
    X = [[12,7],
        [4 ,5],
        [3 ,8]]

    result = [[0,0,0],
             [0,0,0]]

    # iterate through rows
    for i in range(len(X)):
       # iterate through columns
       for j in range(len(X[0])):
           result[j][i] = X[i][j]

    for r in result:
       print(r)
    print("\n")

#Transpose in place function below works only for M*M matrix where no. of rows = no.of cols, otherwise use zip
def transpose_in_place(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for row in range(num_rows):
        for col in range(row+1, num_rows):
            temp = matrix[col][row]
            matrix[col][row] = matrix[row][col]
            matrix[row][col] = temp
    for i in range(num_rows):
        print(matrix[i])
    print('\n')

# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
def rotate_img_90(img, N):
    for layer in range(N/2):
        for i in range(layer, N-layer-1):
            tmp                         = img[layer][i]
            img[layer][i]               = img[N-i-1][layer]
            img[N-i-1][layer]     = img[N-layer-1][N-i-1]
            img[N-layer-1][N-i-1] = img[i][N-layer-1]
            img[i][N-layer-1]           = tmp
    for i in range(N):
        print(img[i])
    print('\n')

def rotate_img_180(img, N):
    for layer in range(N/2):
        for i in range(layer, N-layer-1):
            tmp                         = img[layer][i]
            img[layer][i]               = img[N-layer-1][N-i-1]
            img[N-layer-1][N-i-1]       = tmp
            tmp                         = img[N-i-1][layer]
            img[N-i-1][layer]           = img[i][N-layer-1]
            img[i][N-layer-1]           = tmp
    for i in range(N):
        print(img[i])
    print('\n')


if __name__ == "__main__":
    img = [[1 ,2 ,3 ],
           [5 ,6 ,7 ],
           [9 ,10,12]]

    transpose()
    transpose_in_place(img)
    #otate_img_90(img, len(img))
    #rotate_img_180(img, len(img))