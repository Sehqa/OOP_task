from cat import Cat


class SlowCat(Cat):
    meow_message = 'meeoow'

    def __init__(self, color):
        self.speed = 100
        self.color = color

    def meow(self):
        print('meeoow')

    def run(self):
        print('Slow cat run')
