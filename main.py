import game_framework
from pico2d import open_canvas, close_canvas
#logo_mode를 임포트하되 이름을 바꾼다. start_mode
import logo_mode as start_mode
open_canvas()
game_framework.run(start_mode)
close_canvas()