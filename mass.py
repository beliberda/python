from random import randint
# Способы названия переменных
# название должно отображать суть переменной. То, что она в себе хранит
# Каждое слово, кроме 1го должно начинаться с заглавной буквы
countJump = 10
# либо разделять слова знаком _
count_jump = 20

# массив (список) объявляется как переменная, но в качестве значения []
# Чтобы обратиться к элементу массива пишем название массива massPrice и в скобках
# указываем порядковый номер элемента в []  -  massPrice[]
massPrice = [[9.8], [6,7], ['я', 'kewpo'], 20, [], 'fewkop', count_jump, countJump,77]
massPrice[2][0] = massPrice[2][0] + ' буду готовить пельмени'

massPrice.append('append')
print(massPrice)

print('massPrice.count() ',massPrice.count(20))
print('massPrice.extend()', massPrice.extend(['20','fwoe']))
print('Длина массива ',len(massPrice))

# for i in range(0,len(massPrice)):
#     massPrice[i] = randint(0,100)

print(massPrice)
