#############################################################
#Date: 21.02.22                                             #
#Programmed by: Luka Henig (luka.henig@gmail.com)           #
#Curse: 100 Days of Code(udemy)                             #
#Description: Litle crossing the street game to learn and   #
#understand python and the Turtle Library                   #
#############################################################

#imports
from turtle import Turtle

#constant
FONT = ("Courier", 20, "normal")

#scoardboard class
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the score on screen, no parameters"""
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increment_level(self):
        """increments level by one, no parameters"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """show the Game Over text in the middle of the screen, no parameters"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)