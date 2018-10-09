#Check if a matrix is same when rotated 180 degrees

rotated = zip(*original[::-1]) #rotates 90 degrees
rotated_180 = zip(*rotated[::-1]) #rotates 90 degrees

matrix=[
         [1,2,3,4,5],
         [6,7,8,9,10],
         [11,12,13,12,11],
         [10,9,8,7,6],
         [5,4,3,2,1]
       ]

def is_same_after_180_deg_rotation(matrix):
    N = len(matrix[0])
    mid_row = int(N/2)
    for row in range(0,mid_row):
        for col in range(0,N):
            if matrix[row][col] != matrix[N-1-row][N-1-col]:
                return False
    for col in range(0,N):
        if matrix[mid_row][col] != matrix[mid_row][N-1-col]:
            return False
    return True

#res=is_same_after_180_deg_rotation(matrix)
#print(res)

def test_is_same_after_180_deg_rotation(matrix):
    return(is_same_after_180_deg_rotation(matrix))

def test_matrix_rotation():
    matrix1=[
         [1,2,3,4,5],
         [6,7,8,9,10],
         [11,12,13,12,11],
         [10,9,8,7,6],
         [5,4,3,2,1]
       ]

    matrix2=[
         [1,2,3],
         [6,7,6],
         [3,2,1]
       ]

    matrix3=[
         [1,2,3,6,5],
         [6,7,8,9,10],
         [11,12,13,12,11],
         [10,9,8,7,6],
         [5,4,3,2,1]
       ]

    matrix4=[
         [1,2,3],
         [6,7,8],
         [3,2,1]
       ]

    exp_out = True
    act_out = test_is_same_after_180_deg_rotation(matrix4)
    print(act_out)
    if exp_out == act_out:
        print 'pass'
    else:
        print 'fail'

test_matrix_rotation()