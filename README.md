Абстракция :

class Cat(Runnable, ABC):

    def jump(self):
        print('jumped at ' + str(self._speed) + ' centimeters')

    @abstractmethod
    def meow(self):
        pass

Метод помечен как абстрактный, т.е. он не имеет реализации и обязан 
быть переопределен в дочернем классе.

Наследование: 

class FastCat(Cat):
 
Класс FastCat наследует все методы и свойства класса Cat (Например метод
run): 
fast_cats = FastCat('black')
fast_cats.run()

Полиморфизм:

Сам язык python максимально расположен к полиморфизму: 

Например в поле _speed можно передать цифру, текст, список и т.д

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