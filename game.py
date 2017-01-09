import sfml as sf

import sheet
import doodle


class Game:
    __window = None
    __hero = None
    __isLeft = False
    __isRight = False

    def __init__(self):
        self.__window = sf.RenderWindow(sf.VideoMode(sheet.WINDOW_SIZE.x, sheet.WINDOW_SIZE.y), sheet.WINDOW_TITLE)
        self.__window.framerate_limit = sheet.WINDOW_FRAME_LIMIT
        self.__window.vertical_synchronization = True
        self.__hero = doodle.Doodle()

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
        self.__window.clear(sheet.WHITE)
        self.__hero.draw(self.__window)

    def check_cylinder_effect(self):
        doodle_position = self.__hero.get_position()
        if doodle_position.x <= -sheet.DOODLE_SIZE.x:
            self.__hero.set_position(sf.Vector2(sheet.WINDOW_SIZE.x - sheet.DOODLE_SIZE.x, doodle_position.y))
        if doodle_position.x >= sheet.WINDOW_SIZE.x:
            self.__hero.set_position(sf.Vector2(0, doodle_position.y))
