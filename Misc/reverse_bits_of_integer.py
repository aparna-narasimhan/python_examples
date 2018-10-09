#https://www.youtube.com/watch?v=gxRB6DOQDOQ
def toggleBits(num):
    if num == 0:
        return 1
    solution = 0
    nextSetBit = 1
    while num !=0:
        lastBit = num & 1
        if lastBit == 0:
            solution |= nextSetBit
        nextSetBit = nextSetBit << 1
        num = num >> 1
    return solution