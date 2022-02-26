"""
YOUR FILE's DOC STRING GOES HERE.
"""
import turtle as t
import math


PEN_WIDTH = 2
SIDE = 100

def init():
    t.speed( 2 )
    t.up()
    t.setpos( -50, -200 )
    t.down()
    t.speed( 0 )
    t.pensize( PEN_WIDTH )
    t.down()

number = math.sqrt( 2)/2

def draw_baobab_1( side ):
    t.fd( side )
    t.left( 90 )
    t.fd( side )
    t.left( 90 )
    t.fd( side )
    t.right( 135 )
    t.fd( side * number )
    t.right( 90 )
    t.fd( side * number)
    t.right( 135 )
    t.fd( side )
    t.left( 90 )
    t.fd( side )
    t.left( 90 )


def draw_baobab_2( side ):
    t.left(90)
    t.penup()
    t.fd(side)
    t.right(45)
    t.pendown()
    draw_baobab_1( number * side )
    t.fd(number*side)
    t.right(90)
    draw_baobab_1(number * side)
    t.right(90)
    t.fd(number*side)
    t.left(45)
    t.penup()
    t.fd(side)
    t.left(90)
    t.pendown()
    draw_baobab_1(side)

def draw_baobab_3( side ):
    t.left(90)
    t.penup()
    t.fd( side )
    t.right(45)
    t.pendown()
    draw_baobab_2( number * side )
    t.fd( number * side )
    t.right(90)
    draw_baobab_2(number * side)
    t.right(90)
    t.fd(number * side)
    t.left(45)
    t.penup()
    t.fd( side )
    t.left(90)
    t.pendown()
    draw_baobab_1( side )

def draw_baobab_rec( side, depth ):
    if depth == 0 :
        pass
    if depth == 1 :
        return draw_baobab_1( side )
    if depth >= 2 :
        t.left(90)
        t.penup()
        t.fd(side)
        t.right(45)
        t.pendown()
        draw_baobab_rec(number * side, depth - 1)
        t.fd(number * side)
        t.right(90)
        draw_baobab_rec(number * side, depth - 1)
        t.right(90)
        t.fd(number * side)
        t.left(45)
        t.penup()
        t.fd(side)
        t.left(90)
        t.pendown()
        draw_baobab_1(side)

def main():
    init()
    print( "Drawing a depth-1 baobab drawing." )
    draw_baobab_1( SIDE )
    input( "Hit ENTER to proceed to depth 2:" )
    t.clear()
    draw_baobab_2( SIDE )
    input( "Hit ENTER to proceed to depth 3:" )
    t.clear()
    draw_baobab_3( SIDE )
    input( "Hit ENTER to proceed to recursive code:" )
    t.clear()
    depth = int( input( "depth? " ) )
    draw_baobab_rec( SIDE, depth )
    print( "Close the window to end the program." )
    t.done()


if __name__ == '__main__':
    main()