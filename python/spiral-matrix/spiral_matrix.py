def spiral_matrix(size):

    matrix = []
    firstLine = [x for x in range(1, size+1)]
    lastLine = [x for x in range( 3 * size - 2 , 2 * size - 2 , -1 )]

    if size ==0:
        return matrix 
    elif size == 1:
        matrix.append(firstLine)
        return firstLine
    elif size == 2:
        matrix.append(firstLine)
        matrix.append(lastLine)
        return matrix

#    for x in range(size,1,-2):
#        if x % 2 == 1: