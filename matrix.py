def print_matrix( matrix ):
    for i in range(len(matrix[0])):
        line = ''
        for j in range(len(matrix)):
            line += '%d ' % matrix[j][i]
        print line

def ident( matrix ):
    rows = len(matrix)
    ret = new_matrix(rows, rows)
    for x in range(rows):
        ret[x][x] = 1
    return ret

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for i in range(len(m2)):
        tmp = []
        for j in range(len(m2[0])):
            row = []
            for h in range(len(m1)):
                row.append(m1[h][j])
            tmp.append(dot_product(row, m2[i]))
        m2[i] = tmp

def dot_product(row, col):
    ret = 0
    for i, j in zip(row, col):
        ret += i * j
    return ret

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
