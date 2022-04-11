from params import *


class Uley:
    """
    Класс улья является синглтоном т.е. экземпляра данного
    класса не может быть больше 1. Данный экземпляр будет исполь-
    зован для хранения экземпляров других классов. Serial_number 
    показывает порядковый номер последнего экземпляра пчелы в данный момент.
    """        
    list_of_egg = []
    list_of_lichinka = []
    list_of_bees = []
    queen_bee = object
    male_bees = []
    worker_bees = []

    dead_bodies = []
    amount_of_honey = START_HONEY
    serial_number = 0
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Uley, cls).__new__(cls)
        return cls.instance


class Pchela:
    """
    Каждая пчела рождается при создании экземляра,
    возраст в начале 0.Начальное значение голода равно 100. 
    Все пчелы живые изначально, поэтому значение alive = True
    """
    age = 0 
    alive = BEES_ALIVE
    hunger = 100

    def __init__(self,nomer,weight,max_age)-> int:
        self.no_of_bee = nomer
        self.weight = weight
        self.max_age = max_age

    def aging(self):
        self.age += 1

    def getting_hungry(self):
        self.hunger -= 1

    def eating(self, food):
        self.hunger += food

    def is_alive(self):
        if self.age > self.max_age or self.hunger < 0:
            self.alive = False
        return self.alive


class Queen(Pchela):
    def __init__(self, nomer, weight = 30,max_age= QUEEN_MAX_AGE) -> int:
        super().__init__( nomer, weight,max_age)

    def egg_making(self):
        if self.hunger>10:
            hunger -= 2
            return True
        else:
            return False


class Male(Pchela):
    def __init__(self, nomer, weight = 15, max_age = MALE_MAX_AGE ) -> int:
        weight = 10
        super().__init__( nomer, weight, max_age)
        self.sperm_left = MALE_SPERM_NUMBER
    
    def egg_fertilizing(self):
        self.sperm_left -= 1

    def can_fertilize(self):  # трутней без спермы убивают
        if self.sperm_left <=0:
            self.alive = False
            return False
        else:
            return True


class Worker(Pchela):
    def __init__(self, nomer, weight = 10, max_age = WORKER_MAX_AGE) -> int:
        super().__init__( nomer, weight, max_age)
           
    
    def cleaning(self):
        pass

    def breeding(self):
        pass


class Egg:
    age = 0
    fertilized = False
        
    def aging(self):
        if self.fertilized:
            self.age += 1   

    def fertilization(self):
        self.fertilized = True
    

class Lichinka:
    def __init__(self,typ) -> None:
        self.age = 0
        self.type_of_lichinka = 'Трутень' if typ>=93 else 'Рабочая'

    