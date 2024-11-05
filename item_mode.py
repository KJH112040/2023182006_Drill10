import pico2d

import game_framework
from pico2d import load_image, get_events, clear_canvas, update_canvas
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE
import play_mode
import game_world


class Pannel:
    def __init__(self):
        self.image = load_image('item_select.png')
    pass


def init():
    global pannel
    pannel = Pannel()
    game_world.add_object(pannel,3)
    #image = load_image('item_select.png')

def finish():
    game_world.remove_object(pannel)

def handle_events():
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_mode()
                case pico2d.SDLK_0:
                    play_mode.boy.item = None
                    game_framework.pop_mode()
                case pico2d.SDLK_1:
                    play_mode.boy.item = 'Ball'
                    game_framework.pop_mode()
                case pico2d.SDLK_2:
                    play_mode.boy.item = 'BigBall'
                    game_framework.pop_mode()

def update():
    pass

def draw():
    clear_canvas()
    pannel.image.draw(400,300)
    update_canvas()