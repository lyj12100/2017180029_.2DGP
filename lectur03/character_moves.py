from pico2d import *
import math

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')


x=0
y=80
r=250
pi=math.pi

grass.draw_now(400,30)
character.draw_now(x,y)

while(True):

  
    
    while(x<800-50):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x=x+2
        delay(0.005)
    while(y<600-50):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y+2
        delay(0.005)
    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-2
        delay(0.005)
    while(y>80):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y-2
        delay(0.005)
   

    for degree in range(0,360):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=r*math.sin(degree*pi/180)+400
        y=r*math.cos(degree*pi/180)+300
        delay(0.01)
  
    y=80
    x=0




close_canvas()
