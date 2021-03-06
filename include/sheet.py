import sfml as sf

from enum import Enum


class DirectionX(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2

WINDOW_SIZE = sf.Vector2(600, 800)
WINDOW_TITLE = "DoodleJump"
WINDOW_FRAME_LIMIT = 60

DOODLE_SIZE = sf.Vector2(50, 80)
DOODLE_INITIAL_POSITION = (WINDOW_SIZE  - DOODLE_SIZE) / 2

STEP = 6

GREEN = sf.Color(0, 127, 0)
WHITE = sf.Color(255, 255, 255)
