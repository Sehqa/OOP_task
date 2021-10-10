Абстракция :

class Cat(Runnable, ABC):


    @abstractmethod
    def meow(self):
        pass

Метод помечен как абстрактный, т.е. он не имеет реализации и обязан 
быть переопределен в дочернем классе.

Наследование: 
    class Cat(Runnable, ABC):
         def run(self):
            print('Cat run')
        
    class FastCat(Cat):
        
Класс FastCat наследует все методы и свойства класса Cat (Например метод
run): 

    fast_cats = FastCat('black')
    fast_cats.run()

Полиморфизм:

Сам язык python максимально расположен к полиморфизму: 

Например в поле _speed, через метод set_speed можно передать цифру, текст, список и т.д

    fast_cats = FastCat('black')
    fast_cats.set_speed(1)
    fast_cats.set_speed('text')
    fast_cats.set_speed([1,2,3,4,56])

Инкапсуляция : 

В коде принцип инкапсуляции реализован при помощи get/set 
а так же при помощи подчеркивания перед полями или методами

    def set_speed(self, speed):
        self._speed = speed

    def get_speed(self):
        return self._speed

    @abstractmethod
    def _meow(self):
        pass
