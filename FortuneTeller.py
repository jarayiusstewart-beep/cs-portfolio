# Project: Fortune Teller App (Python with Processing)
# Author: [Your Name]
# Description: A visual fortune teller program where the user clicks a button to receive a random fortune.
#              The app includes a colorful circular pattern background and shows mouse coordinates for interactivity.

from processing import *
from collide2d import *
import random

randomfortunes = []

def setup():
    size(510, 350)
    global randomfortunes
    # List of fortunes
    randomfortunes = [
        "Tomorrow you die after being hit by a car",
        "Tomorrow you will become rich after winning the lottery",
        "Tomorrow you will get married after falling in love"
    ]
    background(255)

# Function to draw colorful circular pattern
def circDesign(x, y):
    starcolor = color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    fill(starcolor)
    noStroke()
    x_pos = 0
    while x_pos < 1050:
        ellipse(x_pos, y, 10, 10)
        x_pos += 50

def draw():
    # Show mouse coordinates
    text(str(mouseX) + ", " + str(mouseY), 20, 20)
    
    # Draw "Fortune" button
    noFill()
    stroke(0)
    rect(220, 175, 60, 20)
    
    # If button clicked, show random fortune
    if collidePointRect(mouseX, mouseY, 220, 175, 60, 20) and mousePressed:
        background(255)
        fortune = random.choice(randomfortunes)
        text(fortune, 140, 140)
        print(fortune)
    
    # Draw button label
    fill(0)
    text("Fortune", 230, 190)
    
    # Draw background pattern
    for x in range(10, width, 50):
        for y in range(10, width, 50):
            circDesign(x, y)

run()
