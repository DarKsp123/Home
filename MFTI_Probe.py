import turtle as tr

# TODO Рисуем букву S
# tr.shape('turtle')
# tr.forward(50)
# tr.left(90)
# tr.forward(50)
# tr.left(90)
# tr.forward(50)
# tr.right(90)
# tr.forward(50)
# tr.right(90)
# tr.forward(50)

# TODO Рисуем квадрат
# tr.shape('turtle')
# tr.forward(100)
# tr.left(90)
# tr.forward(100)
# tr.left(90)
# tr.forward(100)
# tr.left(90)
# tr.forward(100)

# TODO Нарисуйте окружность как пример правильный многоугольник выглядит как круг
# tr.shape('turtle')
# for i in range(25):
#    tr.forward(5)
#    tr.left(5)
#    tr.forward(5)
#    tr.left(5)
#    tr.forward(5)
#    tr.left(5)
#    tr.forward(5)

# TODO Нарисуйте 10 вложенных квадратов
# tr.shape('turtle')
# tr.forward(100)
# tr.left(90)
# tr.forward(100)
# tr.left(90)
# tr.forward(100)
# tr.left(90)
# tr.forward(100)
# tr.penup()
# tr.goto(-5, -5)
# tr.pendown()
# tr.left(90)
# tr.forward(110)
# tr.left(90)
# tr.forward(110)
# tr.left(90)
# tr.forward(110)
# tr.left(90)
# tr.forward(110)
# tr.done()

from math import pi, sin, cos

tr.shape('turtle')
for i in range(200):
    t = i / 10 * pi
    dx = t * cos(t)
    dy = t * sin(t)
    tr.goto(dx, dy)
tr.done()