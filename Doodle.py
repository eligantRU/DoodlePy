import sfml as sf

WINDOW_SIZE = sf.Vector2(600, 800)
WINDOW_TITLE = "DoodleJump"
WINDOW_FRAME_LIMIT = 60

DOODLE_SIZE = sf.Vector2(50, 80)
DOODLE_INITIAL_POSITION = (WINDOW_SIZE  - DOODLE_SIZE) / 2

STEP = 6

GREEN = sf.Color(0, 127, 0)
WHITE = sf.Color(255, 255, 255)


class Doodle:
    __body = None
    __dir = None

    def __init__(self):
        self.__body = sf.RectangleShape()
        self.__body.fill_color = GREEN
        self.__body.size = DOODLE_SIZE
        self.__body.position = DOODLE_INITIAL_POSITION

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
            self.set_direction(0)
        elif is_left:
            self.set_direction(1)
        elif is_right:
            self.set_direction(2)
        else:
            self.set_direction(0)

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
        if direction == 1:
            position_x -= STEP
        elif direction == 2:
            position_x += STEP
        return position_x


class Game:
    __window = None
    __hero = None
    __isLeft = False
    __isRight = False

    def __init__(self):
        self.__window = sf.RenderWindow(sf.VideoMode(WINDOW_SIZE.x, WINDOW_SIZE.y), WINDOW_TITLE)
        self.__window.framerate_limit = WINDOW_FRAME_LIMIT
        self.__window.vertical_synchronization = True
        self.__hero = Doodle()

    def do_game_loop(self):
        while self.__window.is_open:
            self.check_events()
            self.update()
            self.render()
            self.__window.display()

    def check_events(self):
        for event in self.__window.events:
            self.check_keyboard_events(event)
            if type(event) is sf.CloseEvent:
                self.__window.close()

    def check_keyboard_events(self, event):
        is_need_update1 = self.check_key_pressed(event)
        is_need_update2 = self.check_key_released(event)
        if is_need_update1 or is_need_update2:
            self.__hero.update_direction(self.__isLeft, self.__isRight)

    def check_key_pressed(self, event):
        is_need_update = False
        if type(event) is sf.KeyEvent and event.pressed:
            if event.code == sf.Keyboard.A:
                self.__isLeft = True
                is_need_update = True
            elif event.code == sf.Keyboard.D:
                self.__isRight = True
                is_need_update = True
        return is_need_update

    def check_key_released(self, event):
        is_need_update = False
        if type(event) is sf.KeyEvent and event.released:
            if event.code == sf.Keyboard.A:
                self.__isLeft = False
                is_need_update = True
            elif event.code == sf.Keyboard.D:
                self.__isRight = False
                is_need_update = True
        return is_need_update

    def update(self):
        self.__hero.update()
        self.check_cylinder_effect()

    def render(self):
        self.__window.clear(WHITE)
        self.__hero.draw(self.__window)

    def check_cylinder_effect(self):
        doodle_position = self.__hero.get_position()
        if doodle_position.x <= -DOODLE_SIZE.x:
            self.__hero.set_position(sf.Vector2(WINDOW_SIZE.x - DOODLE_SIZE.x, doodle_position.y))
        if doodle_position.x >= WINDOW_SIZE.x:
            self.__hero.set_position(sf.Vector2(0, doodle_position.y))


game = Game()
game.do_game_loop()
