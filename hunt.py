from turtle import *
from random import randint as r
from random import choice as c

def draw_border():
    b = Turtle()
    b.speed(0)
    b.hideturtle()
    b.color("light blue")
    b.goto(-300,300)
    b.begin_fill()
    for side in range(4):
        b.forward(600)
        b.right(90)
    b.end_fill()

class Veggie(Turtle):
    def __init__(self, x, y, img):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.x = x
        self.y = y
        self.goto(x,y)
        self.shape(img)
        self.showturtle()

    def move(self):
        self.x += r(-1,1)
        self.y += r(-1,1)
        if self.x > 300:
            self.x = 295
        if self.x < -300:
            self.x = -295
        if self.y > 300:
            self.y = 295
        if self.y < -300:
            self.y = -295
        self.goto(self.x, self.y)

class Predator(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(x,y)
        self.shape("images/hawk.gif")
        self.setheading(r(0,360))
        self.showturtle()

    def move(self):
        if self.xcor() > 285 or self.xcor() < -285:
            self.setheading(self.heading()-180)
        if self.ycor() > 285 or self.ycor() < -285:
            self.setheading(-1*self.heading())
        self.forward(5)
    
class Rabbit(Turtle):
    def __init__(self, screen):
        super().__init__()
        print("Check")
        self.speed(0)
        self.shape("images/bunny.gif")
        self.penup()
        self.screen = screen
        self.screen.onkeypress(self.turn_right, "Right")
        self.screen.onkeypress(self.turn_left, "Left")

    
    def turn_right(self):
        self.right(10)
    
    def turn_left(self):
        self.left(10)



screen = Screen()
screen.tracer(0)
screen.listen()
screen.bgcolor("black")
screen.register_shape("images/lettuce.gif")
screen.register_shape("images/carrot.gif")
screen.register_shape("images/hawk.gif")
screen.register_shape("images/bunny.gif")
screen.tracer(1)

draw_border()

player = Rabbit(screen)

meals = []
for n in range(10):
    meals.append(Veggie(r(-295,295),r(-295,295), c(["images/lettuce.gif","images/carrot.gif"])))

predators = []
for n in range(5):
    predators.append(Predator(r(-295,295),r(-295,295)))

while True:
    for food in meals:
        food.move()
    
    for hawk in predators:
        hawk.move()
    
    player.forward(2)

screen.mainloop()