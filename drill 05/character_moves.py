from pico2d import *

open_canvas()
grass=load_image('grass.png')
character=load_image('animation_sheet.png')

def firstpos():
    frame=0
    count=0
    x,y=203,535
    nextx,nexty=132,243
    nextposx,nextposy=(nextx-x)/50 ,(nexty-y)/50
    while count<50:
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,0,100,100,x,y)
        update_canvas()
        count+=1
        x+=nextposx
        y+=nextposy
        frame=(frame+1)%8
        delay(0.05)

def go_secondpos():
    frame = 0
    count = 0
    x, y = 132, 243
    nextx,nexty=535,470
    nextposx, nextposy = (nextx-x) / 50, (nexty-y) / 50
    while count < 50:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        count += 1
        x += nextposx
        y += nextposy
        frame = (frame + 1) % 8
        delay(0.05)

def go_thirdpos():
    frame = 0
    count = 0
    x, y = 535, 470
    nextx,nexty=477,203
    nextposx, nextposy = (nextx-x) / 50, (nexty-y) / 50
    while count < 50:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        count += 1
        x += nextposx
        y += nextposy
        frame = (frame + 1) % 8
        delay(0.05)

def go_fourthpos():
    frame = 0
    count = 0
    x, y = 477, 203
    nextx , nexty=715,136
    nextposx, nextposy = (nextx-x) / 50, (nexty-y) / 50
    while count < 50:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        count += 1
        x += nextposx
        y += nextposy
        frame = (frame + 1) % 8
        delay(0.05)

def go_fifthpos():
    frame = 0
    count = 0
    x, y = 715,136
    nextx, nexty = 316,225
    nextposx, nextposy = (nextx - x) / 50, (nexty - y) / 50
    while count < 50:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        count += 1
        x += nextposx
        y += nextposy
        frame = (frame + 1) % 8
        delay(0.05)


while True:
    firstpos()
    go_secondpos()
    go_thirdpos()
    go_fourthpos()
    go_fifthpos()

close_canvas()