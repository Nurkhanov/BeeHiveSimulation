from models import Uley,Lichinka,Egg,Queen,Worker,Male
from general_funcs import *
import datetime
import time
from random import randint

# eda = 10000
# Pchela_1 = Pchela(1,1,10,100,0)

# Matka = Pchela(1,1,20,100,0)


# while Pchela_1.is_alive():
#     print(f'{Pchela_1.age}    {Pchela_1.hungry}')
#     Pchela_1.hunger()
#     Pchela_1.aging()
#     if Pchela_1.hungry < 10:
#         if  eda > Pchela_1.weight > 0:
#             Pchela_1.eating(Pchela_1.weight)
#             eda -= Pchela_1.weight
#         elif eda > 0:
#             Pchela_1.eating(eda)
#             eda -= eda
#         else: 
#             pass
# # Иницализация улья
Dom = Uley()
adding_to_uley(Queen)
adding_to_uley(Worker,1000)
adding_to_uley(Male)


# for i in range(10):
#     eggs_1.append(Lichinka(randint(0,100)))
#     print(eggs_1[i].type_of_lichinka)
ticks_count = 0

while bool(Uley.list_of_bees): # цикл будет остановлен когда все пчелы умрут
    all_bees_getting_hungry()  #каждый тик у пчел растет голод на 1 ед.
    all_hungry_bees_eating()   
    dead_bee_list_replace()     
    
    if ticks_count%10==0:      # каждые 10 тиков все пчелы стареют на 1 ед.
        all_bees_aging()
        all_bees_working()
        print(f'Прошло {ticks_count//10} дней')
    
    print(f'Количество пчел:{len(Uley.list_of_bees)} Трупы:{len(Uley.dead_bodies)}  Еда: {Uley.instance.amount_of_honey}')
    ticks_count +=1
    time.sleep(0.1)
