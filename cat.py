from abc import ABC, abstractmethod
from threading import Thread


class Runnable(ABC):

    @abstractmethod
    def run(self):
        pass


class Cat(Runnable, ABC):

    def set_color(self, color):
        self._color = color

    def set_speed(self, speed):
        self._speed = speed

    def get_color(self):
        return self._color

    def get_speed(self):
        return self._speed

    def jump(self):
        print('jumped at ' + str(self._speed) + ' centimeters')

    @abstractmethod
    def _meow(self):
        pass

    def run(self):
        print('Cat run')

    def hearVacuumCleaner(self):
        meow_thread = Thread(target=self.meow())
        run_thread = Thread(target=self.run())
        messages_thread = Thread(target=print('Furious cat'))
        meow_thread.start()
        run_thread.start()
        messages_thread.start()
