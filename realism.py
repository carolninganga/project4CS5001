# Caroline Ninganga
# CS 5001

# line 5 and 6 import the complex_shapes and the graphicsPlus 
import complex_shapes as cs
import graphicsPlus as gr

import sys

def scene( argsList ): 
 
    # this is the graphics window
    win = gr.GraphWin( "My window", 1000, 1000 )

    x = 0
    y = 0
    scale = 1

    if len(argsList) == 4:
        x = int (argsList[1])
        y = int (argsList[2])
        scale = int (argsList[3])

    print(argsList)


    # draw the man into the window 
    man = cs.init_man( x, y, scale)

    # draw the sun into the window
    sun = cs.init_sun( x, y, scale)

    # draw the pool into the window
    pool = cs.init_pool( x, y, scale)

    # line 22 to 24 call the draw function which draws the zelle shapes that draw the complex shapes 
    cs.draw(man, win)
    cs.draw(sun, win)
    cs.draw(pool, win)

    # pause until user gets mouse
    # c.undraw()

   
    # wait for a mouse click
    win.getMouse()
    # close the window
    win.close()

if __name__ == "__main__":
    scene(sys.argv)