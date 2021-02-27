# Caroline Ninganga
# CS 5001
# Project 4
# Man on a ship

import graphicsPlus as gr

# def init_man defines the pool fucntion with three parameters x, y and scales
def init_man(x, y, scale):
    # define the man shapes and put them into a list

    # Head: Create a circle with the color brown
    head = gr.Circle( gr.Point ( x+scale*10, y-scale*50), 20*scale) 
    head.setFill('brown')

    # arms : Create a rectangle with the color blue for the arms
    arms = gr.Rectangle( gr.Point ( x+scale*110, y), gr.Point(x-scale*80, y-scale*30 ))
    arms.setFill('blue')

    # stomach : Create a rectangle with the color blue for the sh 
    stomach = gr.Rectangle( gr.Point ( x+scale*70, y+scale*60), gr.Point(x-scale*50, y ))
    stomach.setFill('blue')

    # # leg2 : Create a rectangle with the color red for pants
    leg1 = gr.Rectangle( gr.Point ( x-scale*20, y+scale*60), gr.Point(x-scale*40, y+scale*180 ))
    leg1.setFill('red')

    #   # leg2 : Create a rectangle with the color red for pants 
    leg2 = gr.Rectangle( gr.Point ( x+scale*60, y+scale*60), gr.Point(x+scale*40, y+scale*180 ))
    leg2.setFill('red')

  
    # man creates the list of all the basic shapes created by zelle
    man = [ head, arms, leg1, leg2, stomach ]
    return man

# define the test man function which asigns the different sizes and locations of the man it also calls the draw function passing two arguments
def test_man():
    win = gr.GraphWin( "My window", 1500, 1500 )
    
    man1 = init_man(300, 300, 1)
    man2 = init_man(250, 250, 0.5)
    man3 = init_man(400, 400, 2)

# The draw function which carries two arguments, first is the sun1 which is the list of zelle shapes which makes objects
    draw(man1, win)
    draw(man2, win)
    draw(man3, win)

    win.getMouse()
    win.close()

# def init_sun defines the pool fucntion with three parameters x, y and scales
def init_sun(x, y, scale):
     # create a circle with the sun
    inner_sun = gr.Circle( gr.Point ( x-scale*260, y-scale*200), 120*scale) 
    inner_sun.setFill('orange')

    outer_sun= gr.Circle( gr.Point ( x-scale*260, y-scale*200), 150*scale) 
    outer_sun.setFill('yellow')

    # leg1 = gr.Rectangle( gr.Point ( x-scale*20, y+scale*60), gr.Point(x-scale*40, y+scale*180 ))
    # leg1.setFill('red')

    
    sun = [ outer_sun, inner_sun ]
    return sun

# define the test sun function which asigns the different sizes and locations of the sun it also calls the draw function passing two arguments
def test_sun():
    win = gr.GraphWin( "My window", 1500, 1500 )

    sun1 = init_sun(300, 300, 1)
    sun2 = init_sun(250, 2500, 0.5)
    sun3 = init_sun(400, 400, 2)
# The draw function which carries two arguments, first is the sun1 which is the list of zelle shapes which makes objects
    draw(sun1, win)
    draw(sun2, win)
    draw(sun3, win)

    win.getMouse()
    win.close()

# def init_pool defines the pool fucntion with three parameters x, y and scales
def init_pool(x, y, scale):

    # # diving board : Create a rectangle with the color brown 
    diving_board = gr.Rectangle( gr.Point ( x+scale*180, y+scale*180), gr.Point(x-scale*260, y+scale*250 ))
    diving_board.setFill('brown')

    # create a swiming pool with the color skyblue
    water = gr.Rectangle( gr.Point ( x+scale*780, y+scale*880), gr.Point(x-scale*260, y+scale*250 ))
    water.setFill('skyblue')

    # create a list of the complex shapes 
    pool = [  diving_board, water ]

    return pool

def test_pool():
    win = gr.GraphWin( "My window", 1000, 1000 )

    pool1 = init_pool(300, 300, 1)
    pool2 = init_pool(250, 250, 0.5)
    pool3 = init_pool(400, 400, 2)

# The draw function which carries two arguments, first is the sun1 which is the list of zelle shapes which makes objects
    draw(pool1, win)
    draw(pool2, win)
    draw(pool3, win)

    win.getMouse()
    win.close()


#  shapes is a list of zelle objects that make a complex shape
def draw( shapes, win ):

    for thing in shapes:
        thing.draw( win )

    

if __name__ == "__main__":
    test_man()

