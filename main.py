from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 255 ]

def test_multiplication():
    edges = new_matrix(4, 0)
    add_edge(edges, 0, 0, 1, 200, 200, 1)
    add_edge(edges, 200, 200, 1, 200, 300, 1)
    print 'Edges: '
    print_matrix(edges)

    ident_matrix = ident(edges)
    print 'Identity Matrix for edges:'
    print_matrix(ident_matrix)

    transform_right = ident(edges)
    transform_right[3] = [50, 0, 0, 1]
    print 'Transformation Matrix (+50, +0):'
    print_matrix(transform_right)

    matrix_mult(transform_right, edges)
    print 'Edges after multiplying with transformation matrix:'
    print_matrix(edges)

def draw_stuff():
    edges = new_matrix(4, 0)
    # hexagons
    for offset in range(-25, 25, 10):
        add_edge(edges, 0 + offset, 180, 1, 180 + offset, 100 - offset, 1)
        add_edge(edges, 180 + offset, 100 - offset, 1, 180 - offset, -100 - offset, 1)
        add_edge(edges, 180 - offset, -100 - offset, 1, 0 - offset, -180, 1)
        add_edge(edges, 0 - offset, -180, 1, -180 - offset, -100 + offset, 1)
        add_edge(edges, -180 - offset, -100 + offset, 1, -180 + offset, 100 + offset, 1)
        add_edge(edges, -180 + offset, 100 + offset, 1, 0 + offset, 180, 1)

    # s
    add_edge(edges, 80, 80, 1, -80, 80, 1)
    add_edge(edges, -80, 80, 1, -80, 20, 1)
    add_edge(edges, -80, 20, 1, 80, -20, 1)
    add_edge(edges, 80, -20, 1, 80, -80, 1)
    add_edge(edges, 80, -80, 1, -80, -80, 1)

    transform = ident(new_matrix())
    transform[3] = [250, 250, 0, 1]
    matrix_mult(transform, edges)
    #print 'Drawing edges:'
    #print_matrix(edges)
    draw_lines( edges, screen, color )
    display(screen)

def test_lines():
    edges = new_matrix(4, 0)
    x0 = 250
    y0 = 250
    x1 = 200
    y1 = 300
    while x1 <= 300:
        add_edge(edges, x0, y0, 1, x1, y1, 1)
        x1 += 10
    while y1 >= 200:
        add_edge(edges, x0, y0, 1, x1, y1, 1)
        y1 -= 10
    while x1 >= 200:
        add_edge(edges, x0, y0, 1, x1, y1, 1)
        x1 -= 10
    while y1 <= 300:
        add_edge(edges, x0, y0, 1, x1, y1, 1)
        y1 += 10
    #print_matrix(edges)
    draw_lines( edges, screen, color )
    display(screen)

if __name__ == '__main__':
    test_multiplication()
    #test_lines()
    draw_stuff()
    #save_ppm(screen, 'stuyhacks.ppm')
