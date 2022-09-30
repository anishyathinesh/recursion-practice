import turtle as tt


def hexagons(side,num):
    tt.up()
    tt.backward(num*side)
    tt.down()
    for i in range(0,num):
        for j in range(0,6):
            tt.forward(side)
            tt.left(60)
        tt.up()
        tt.forward(side*2)
        tt.down()


def center_pyramid(height, side):
    tt.up()
    tt.backward((height * side) / 2)
    tt.down()


def pyramid(side, height):
    if height == 0:
        pass
    else:
        for i in range(height):
            for i in range(3):
                tt.forward(side)
                tt.left(120)
            tt.forward(side)
        tt.up()
        tt.left(90)
        tt.forward(side)
        tt.right(90)
        tt.backward((height*side) - (side/2))
        tt.down()
        pyramid(side, height-1)


if __name__ == "__main__":
    hexagons(50, 5)
    tt.clear()
    tt.up()
    tt.goto(0,0)
    tt.down()
    center_pyramid(50,5)
    pyramid(50,5)
    tt.done()


