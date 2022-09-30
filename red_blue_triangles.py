import turtle as tt


def draw_triangle(size):
    tt.forward(size)
    tt.left(120)
    tt.forward(size)
    tt.left(120)
    tt.forward(size)
    tt.left(120)


def triangle(size, depth):
    if depth == 0:
        pass
    else:
        tt.begin_fill()
        tt.fillcolor("blue" if depth % 2 else "red")
        draw_triangle(size)
        tt.end_fill()

        tt.forward(size)
        tt.left(120)
        tt.forward(size/2)
        tt.left(60)
        triangle(size/2, depth-1)

        tt.right(60)
        tt.backward(size/2)
        tt.right(120)
        tt.backward(size)


if __name__ == "__main__":
    triangle(200, 4)



