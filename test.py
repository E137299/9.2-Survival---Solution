from turtle import * 
from random import randint as r
import random

############# DEFINE CLASSES AND FUNCTIONS #############
def road():
    r = Turtle()
    r.hideturtle()
    r.speed(0)
    r.goto(-160,500)
    r.fillcolor("gray")
    r.begin_fill()
    r.goto(160,500)
    r.goto(160,-500)
    r.goto(-160,-500)
    r.end_fill()



class Car(Turtle):
    def __init__(self,shp):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(random.choice([0, 30, -30, 60,-60, 90, -90, 120, -120, 150, -150]),random.choice([350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200]))
        self.showturtle()
        self.shape(shp)
        self.setheading(-90)
        self.speed = 15

    def move(self):
        self.forward(self.speed)
        if self.ycor() < -400:
            print("Bottom")
            self.respawn()
            print("Spawn")

    def respawn(self):
        print("ll")
        self.hideturtle()
        self.goto(random.choice([0, 30, -30, 60,-60, 90, -90, 120, -120, 150, -150]),r(500,900))
        self.showturtle()

class Player(Turtle):
    def __init__(self, traffic):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.traffic = traffic
        self.goto(0,-250)
        self.shape("images/one.gif")
        self.showturtle()
        screen.onkeypress(self.move_right, "Right")
        screen.onkeypress(self.move_left, "Left")
        screen.onkeypress(self.accelerate,"Up")
        screen.onkeypress(self.deccelerate, "Down")

    def move_right(self):
        self.setx(self.xcor()+10)
    
    def move_left(self):
        self.setx(self.xcor()+10)
    
    def accelerate(self):
        for car in traffic:
            car.speed += 5

    def deccelerate(self):
        for car in traffic:
            car.speed -= 5




############# YOUR PROGRAM  #############
screen = Screen()
screen.listen()
screen.tracer(0)
screen.bgcolor("green")
road()
screen.register_shape("images/one.gif")
screen.register_shape("images/two.gif")
screen.register_shape("images/three.gif")
screen.register_shape("images/four.gif")
screen.register_shape("images/five.gif")
screen.tracer(1)

images = ["images/one.gif", "images/two.gif", "images/three.gif", "images/four.gif", "images/five.gif"]
traffic = []

for n in range(10):
    car = random.choice(images)
    print(car)
    traffic.append(Car(car))

player = Player(traffic)
while True:
    for car in traffic:
        car.move()