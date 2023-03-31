from random import randint
import time

hp  = 100
speed = 0
rock = 1
yeti = 2
neighbour = 3
totalDistance = 400

def CheckSkill(enemy, hp, speed, num):
        checkSkill = int(input(f'У вас на пути встал {enemy}, куда свернуть? \n1. Влево \n2. Вправо \n'))
        randomNumber = randint(1,2)  
        if (checkSkill == randomNumber):
            print(f'Ты избежал {enemy} на скорости ', speed, ' км/сек' )
        else:
            hp -= num
            print(f'ты столкнулся с {enemy}, осталось: {hp} хп')
            speed = 0


while True:
    if totalDistance <= 0:
        print('Ты победил')
        break
    elif (hp <= 0):
        print('Помер')
        break
    randomNumber = randint(0,10)   
    if randomNumber == yeti:
        CheckSkill('Йети', hp, speed,10)
    elif randomNumber == neighbour:
        CheckSkill('Сосед', hp, speed,20)
    elif randomNumber == rock:
        CheckSkill('Камень', hp, speed,5)

    totalDistance -= speed
    speed+=1
    print('Осталось проехать ', totalDistance)
    time.sleep(0.5)
