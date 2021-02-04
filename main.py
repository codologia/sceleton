import pygame as pg

W_WIDTH = 350
W_HEIGHT = 200

pg.init()
screen = pg.display.set_mode((W_WIDTH, W_HEIGHT))
clock = pg.time.Clock()

running = True
while running:
    clock.tick(30)
    
    list_events = pg.event.get()
    for event in list_events:
        if event.type == pg.QUIT:
            running = False
        
    pg.display.update()

pg.quit()