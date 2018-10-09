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
    img = [[1 ,2 ,3 ,4 ],
           [5 ,6 ,7 ,8 ],
           [9 ,10,11,12],
           [13,14,15,16]]

    #rotate_img_90(img, len(img))
    rotate_img_180(img, len(img))