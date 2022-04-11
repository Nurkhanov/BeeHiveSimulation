from models import Uley,Worker,Egg,Male


def all_bees_aging():
    obj = Uley.instance.list_of_bees
    for i in obj:
        i.aging()

def all_bees_getting_hungry():
    obj = Uley.instance.list_of_bees
    for i in obj:
        i.getting_hungry()

def all_hungry_bees_eating():
    obj = Uley.instance.list_of_bees
    for i in obj:
        if i.hunger<20:
            if Uley.instance.amount_of_honey > i.weight:
                i.eating(i.weight)
                Uley.instance.amount_of_honey -= i.weight
                
            elif Uley.instance.amount_of_honey > 0:
                i.eating(Uley.instance.amount_of_honey)
                Uley.instance.amount_of_honey = 0

def queen_egg_making():
    if Uley.instance.list_of_bees[0].egg_making():
        Uley.instance.list_of_egg.append(Egg())

def dead_bee_list_replace():
    obj_1 = Uley.instance.list_of_bees
    obj_2 = Uley.instance.dead_bodies
    for i in obj_1:
        i.is_alive()
        if not i.alive:
            obj_2.append(i)
            obj_1.remove(i)

def all_bees_working():
    obj = Uley.instance.list_of_bees
    for i in obj:
        if i.__class__==Worker:
            Uley.instance.amount_of_honey += 20

def sum_of_alive_bees():
    obj = []
    for i in Uley.list_of_bees:
        if i.alive:
            obj.append(i)
    return len(obj)
                
def all_eggs_fertilization():
    obj = Uley.instance.list_of_bees
    for i in obj:
        if i.__class__ == Male:
            for i in Uley.instance.list_of_bees:
                pass
#TODO fix this 

def all_eggs_aging():
    pass

def transform_egg_lichinka():
    pass

def all_lichinka_aging():
    pass

def all_lichinka_getting_hungry():
    pass

def transform_lichinka_to_bee():
    pass

def adding_to_uley(cl,repeat = 1)->type:
    """
    Данная фунция автоматически добавляет экземпляр полученного
    класса в список в Улье. Для каждой пчелы присваивается
    уникальный серийный номер по порядку возрастания.
    """
    for i in range(repeat):
        obj = cl(Uley.instance.serial_number)
        Uley.instance.serial_number += 1
        Uley.instance.list_of_bees.append(obj)
    

