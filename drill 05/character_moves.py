from pico2d import *
open_canvas()


grass=load_image('grass.png')
character=load_image('animation_sheet.png')

def firstpos():
    frame=0
    count=0
    x,y=203,535
    nextposx,nextposy=(132-203)/50 ,(243-535)/50
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
    nextposx, nextposy = (535 - 132) / 50, (470 - 243) / 50
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



while True:
    firstpos()
    go_secondpos()

close_canvas()