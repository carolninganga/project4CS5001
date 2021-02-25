# Caroline Ninganga
# CS 5001
# Project 4
# Man on a ship

import graphicsPlus as gr

def init_man(x, y, scale):
    # define the man shapes and put them into a list

    # Head: Create a circle
    head = gr.Circle( gr.Point ( x+scale*10, y-scale*50), 20*scale)  

    # arms : Create a rectangle 
    arms = gr.Rectangle( gr.Point ( x+scale*120, y), gr.Point(x-scale*80, y-scale*30 ))

    # stomach : Create a rectangle 
    stomach = gr.Rectangle( gr.Point ( x+scale*40, y+scale*20), gr.Point(x-scale*50, y-scale*50 ))

    # # leg2 : Create a rectangle 
    # leg1 = gr.Rectangle( gr.Point ( 10, 10), gr.Point(40, 160 ))

    #   # leg2 : Create a rectangle 
    # leg2 = gr.Rectangle( gr.Point ( 40, 40), gr.Point(60, 160 ))


    man = [ head, arms, stomach ]

    return man

def main(): 

    # this is the graphics window
    win = gr.GraphWin( "My window", 1000, 1000 )

    # draw the circle into the window 
    man = init_man( 200, 200, 2)

    for thing in man:
        thing.draw( win )

    # pause until user gets mouse
    # c.setFill( "green" )  
    # c.undraw()

   
    # wait for a mouse click
    win.getMouse()
    # close the window
    win.close()

if __name__ == "__main__":
    main()



#     win.getMouse()
#     win.close()
# #Set the Polygon fill color to be a grey-blue color (150, 170, 200 ).
#     head = gr.Polygon( gr.Point (x-scale*10, y-scale*80), gr.Point(x, y-scale*100 ), gr.Point(x+scale*10, y-scale*80 ) )
#     head.setFill( gr.color_rgb(150, 170, 200 ))

# #L Fin: Create a Polygon, with points (x-scale*10, y), (x-scale*10, y-scale*20 ), and (x- scale*25, y+scale*5 ). 
# #Set the Polygon fill color to be a grey-red color (200, 170, 150 ).
#     left_fin = gr.Polygon( gr.Point(x-scale*10, y), gr.Point(x-scale*10, y-scale*20 ), gr.Point(x- scale*25, y+scale*5 ))
#     left_fin.setFill( gr.color_rgb(200, 170, 150 ))


# #R Fin: Create a Polygon, with points (x+scale*10, y), (x+scale*10, y-scale*20 ), and (x+scale*25, y+scale*5 ). 
# #Set the Polygon fill color to be a grey-red color (200, 170, 150 ).
#     right_fin = gr.Polygon( gr.Point(x+scale*10, y), gr.Point(x+scale*10, y-scale*20 ), gr.Point(x+scale*25, y+scale*5 ) ) 
#     right_fin.setFill( gr.color_rgb(200, 170, 150 ) )


#     rocket = [body, nose, left_fin, right_fin]