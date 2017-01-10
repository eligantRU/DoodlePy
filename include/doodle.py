import sfml as sf

from include import sheet


class Doodle:
    __body = None
    __dir = None

    def __init__(self):
        self.__body = sf.RectangleShape()
        self.__body.fill_color = sheet.GREEN
        self.__body.size = sheet.DOODLE_SIZE
        self.__body.position = sheet.DOODLE_INITIAL_POSITION

    def draw(self, window):
        window.draw(self.__body)

    def move(self, offset):
        self.__body.move(offset)

    def update(self):
        self.move(self.get_offset())

    def set_direction(self, dir):
        self.__dir = dir

    def get_direction(self):
        return self.__dir

    def update_direction(self, is_left, is_right):
        if is_left and is_right:
            self.set_direction(sheet.DirectionX.NONE)
        elif is_left:
            self.set_direction(sheet.DirectionX.LEFT)
        elif is_right:
            self.set_direction(sheet.DirectionX.RIGHT)
        else:
            self.set_direction(sheet.DirectionX.NONE)

    def set_position(self, pos):
        self.__body.position = pos

    def get_position(self):
        return self.__body.position

    def get_offset(self):
        return sf.Vector2(self.get_horizontal_offset(), self.get_vertical_offset())

    def get_vertical_offset(self):
        return 0

    def get_horizontal_offset(self):
        position_x = 0
        direction = self.get_direction()
        if direction == sheet.DirectionX.LEFT:
            position_x -= sheet.STEP
        elif direction == sheet.DirectionX.RIGHT:
            position_x += sheet.STEP
        return position_x
