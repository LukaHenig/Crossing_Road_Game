#############################################################
#Date: 21.02.22                                             #
#Programmed by: Luka Henig (luka.henig@gmail.com)           #
#Curse: 100 Days of Code(udemy)                             #
#Description: Litle crossing the street game to learn and   #
#understand python and the Turtle Library                   #
#############################################################

#imports
from turtle import Turtle, Screen
from player import Player
from car import Car_Manager
from scoreboard import Scoreboard
import time

#constants
WIDTH = 600
HEIGHT = 600

#screen handling
screen = Screen()
screen.bgcolor("white")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Crossing Road")
screen.tracer(0)    #to avoid moving animation

#creat player
player = Player()

#creat car_manager
car_manager = Car_Manager()

#creat scoreboard
scoreboard = Scoreboard()

#player control
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

#Game Loop
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect if turtle reached other side
    if player.cross_street_successfully():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increment_level()

screen.exitonclick()