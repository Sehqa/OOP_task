from cat import Cat


class FastCat(Cat):
    meow_message = 'meow'
    _speed = 200
    _color = ''

    def __init__(self, color):
        self._speed = FastCat._speed
        self._color = color

    def _meow(self):
        print('meow')

    def jump(self):
        print('Fast cats are afraid to jump')
