from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        if random.randint(1, 6) == 6:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))
            car.setheading(180)
            car.car_speed = 0
            self.all_cars.append(car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.forward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
