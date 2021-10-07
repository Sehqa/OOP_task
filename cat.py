from abc import ABC, abstractmethod
from fast_cat import FastCat
from slow_cat import SlowCat


class Runnable(metaclass=ABC):

    @abstractmethod
    def run(self):
        pass


class Cat(ABC, Runnable):

    def jump(self):
        print('jumped at ' + str(self.speed) + ' centimeters')

    @abstractmethod
    def meow(self):
        pass

    def run(self):
        print('Cat run')

    def hearVacuumCleaner(self):
        pass


fast_cats = FastCat('black')
fast_cats.meow()
fast_cats.jump()
slow_cats = SlowCat('white')
slow_cats.meow()
slow_cats.jump()
