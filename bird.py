from pico2d import load_image
from state_machine import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 50.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION=0.5
ACTION_PER_TIME=1.0/TIME_PER_ACTION
FRAMES_PER_ACTION=5

class Bird:
    def __init__(self):
        self.x,self.y = 30, 200
        self.image = load_image('bird_animation.png')
        self.dir=0
        self.w_size, self.h_size = 20,20
    def update(self):
        self.state_machine.update()

    def draw(self):
        self.state_machine.draw()

class left_flying:
    @staticmethod
    def enter(bird):pass
    @staticmethod
    def exit(bird):pass
    @staticmethod
    def do(bird):pass
    @staticmethod
    def draw():pass

class right_flying:
    @staticmethod
    def enter(bird):
        pass

    @staticmethod
    def exit(bird): pass

    @staticmethod
    def do(bird):
        bird.frame= (bird.frame+FRAMES_PER_ACTION*ACTION_PER_TIME*game_framework.frame_time)%5
        bird.x += bird.dir * RUN_SPEED_PPS * game_framework.frame_time

        if bird.x > 1590:
            bird.state_machine.add_event(('left_flying', 0))
        pass

    @staticmethod
    def draw(bird):
        bird.clip_composite_draw(int(bird.frame)*100,bird.yframe*100,100,100,'',bird.x,bird.y,bird.w_size,bird.h_size)
        pass