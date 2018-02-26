from display import *
from matrix import *

def draw_lines( matrix, screen, color ):
    for i in range(0, len(matrix), 2):
        x0 = matrix[i][0]
        y0 = matrix[i][1]
        x1 = matrix[i + 1][0]
        y1 = matrix[i + 1][1]
        #print 'Drawing from (%d, %d) to (%d, %d)' % (x0, y0, x1, y1)
        draw_line(x0, y0, x1, y1, screen, color)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append([x, y, z, 1])

def draw_line( x0, y0, x1, y1, screen, color ):
    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt
    m = 1000
    if x0 == x1 and y1 < y0:
        m = -1000
    elif x0 != x1:
        m = float(y1 - y0) / (x1 - x0)
    if m > 1:
        draw_line_octant2(x0, y0, x1, y1, screen, color)
    elif m > 0:
        draw_line_octant1(x0, y0, x1, y1, screen, color)
    elif m > -1:
        draw_line_octant8(x0, y0, x1, y1, screen, color)
    else:
        draw_line_octant7(x0, y0, x1, y1, screen, color)

def draw_line_octant1(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1

    d = 2*A + B
    while x <= x1:
        plot(screen, color, x, y)
        if d > 0:
            y += 1
            d += 2*B
        x += 1
        d += 2*A

def draw_line_octant2(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1

    d = A + 2*B
    while y <= y1:
        plot(screen, color, x, y)
        if d < 0:
            x += 1
            d += 2*A
        y += 1
        d += 2*B

def draw_line_octant7(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1

    d = A - 2*B
    while y >= y1:
        plot(screen, color, x, y)
        if d > 0:
            x += 1
            d += 2*A
        y -= 1
        d -= 2*B

def draw_line_octant8(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1

    d = 2*A - B
    while x <= x1:
        plot(screen, color, x, y)
        if d < 0:
            y -= 1
            d -= 2*B
        x += 1
        d += 2*A
