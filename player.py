#############################################################
#Date: 21.02.22                                             #
#Programmed by: Luka Henig (luka.henig@gmail.com)           #
#Curse: 100 Days of Code(udemy)                             #
#Description: Litle crossing the street game to learn and   #
#understand python and the Turtle Library                   #
#############################################################

#imports
from turtle import Turtle

#constatns
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#player class
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        """to move the player 10 pixels up, no parameters"""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """to reset the starting position of the player, no parameters"""
        self.goto(STARTING_POSITION)

    def cross_street_successfully(self):
        """check if finish line is reached, no parameters"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False