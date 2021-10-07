from abc import ABC, abstractmethod
from threading import Thread


class Runnable(ABC):

    @abstractmethod
    def run(self):
        pass


class Cat(Runnable):

    def jump(self):
        print('jumped at ' + str(self.speed) + ' centimeters')

    @abstractmethod
    def meow(self):
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
