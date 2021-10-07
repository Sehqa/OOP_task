from cat import Cat
from time import sleep


class FastCat(Cat):
    meow_message = 'meow'

    def __init__(self, color):
        self.speed = 200
        self.color = color

    def meow(self):
        print('meow')

    def jump(self):
        print('Fast cats are afraid to jump')
