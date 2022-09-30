"""
author: anishya m thinesh
recursion review
"""
import turtle as t


def center_cleef(depth, radius):
    t.up()
    t.backward((4*radius) + (radius/3))
    t.down()


def van_cleef(depth, radius):
    if depth == 0:
        pass
    else:
        for i in range(4):
            t.circle(radius, 180)
            t.up()
            t.forward(radius*2)
            t.left(90)
            t.forward(radius*2)
            t.down()
        t.up()
        t.left(90)
        t.forward(radius)
        t.right(90)
        t.backward(radius*3)
        t.down()

        t.up()
        t.right(45)
        t.forward(radius*7)
        t.down()
        t.left(45)

        van_cleef(depth-1, radius/2)

        t.right(45)
        t.up()
        t.backward(radius*7)
        t.down()
        t.left(45)

        t.up()
        t.left(45)
        t.forward(radius*3)
        t.down()
        t.right(45)

        van_cleef(depth-1, radius/2)

        # t.right(45)
        # t.up()
        # t.backward(radius*4)
        # t.down()


if __name__ == "__main__":
    t.speed(0)
    t.pensize(4)
    t.color("lightpink")
    center_cleef(2,40)
    van_cleef(2, 40)

    t.done()