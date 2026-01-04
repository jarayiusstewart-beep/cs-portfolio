# Project: Interactive Drawing App (Python with Processing)
# Author: Jarayius Stewart
# Description: A drawing program where the user can draw lines with the mouse, change colors using on-screen color buttons,
#              and reset the canvas. The app shows the current mouse coordinates and allows different brush weights.

from processing import *
from collide2d import *

theLine = {}

def setup():
    size(1000,1000)
    background(220)
    
    global theLine  # this makes it a global variable
    # theLine is a dictionary for our drawing app
    theLine = {
        "weight": 5,
        "red": 220,
        "green": 220,
        "blue": 220,
        "opacity": 100,
    }

def draw():
    text(str(mouseX) + ", " + str(mouseY), 20, 20)
    strokeWeight(theLine["weight"])
    stroke(theLine["red"], theLine["green"], theLine["blue"])
    if mousePressed:
        line(mouseX, mouseY, pmouseX, pmouseY)

    if 300 < mouseX < 800 and 300 < mouseY < 800:
        theLine["weight"] = 5
        
    fill(255)  # white
    stroke(0)
    rect(0, 800, 1000, 180)
    
    fill(255)  # white
    stroke(0)
    ellipse(475, 950, 50, 50)
    if collidePointCircle(mouseX, mouseY, 475, 950, 50) and mousePressed:
        theLine["red"] = 220
        theLine["green"] = 220
        theLine["blue"] = 220
    
    fill(255)  # white
    stroke(0)
    ellipse(475, 850, 50, 50)
    if collidePointCircle(mouseX, mouseY, 475, 850, 50) and mousePressed:
        theLine["red"] = random(0,255)
        theLine["green"] = random(0,255)
        theLine["blue"] = random(0,255)
    
    fill(255,0,0)  # red
    stroke(color(0,0,0))
    ellipse(250, 900, 100, 100)
    if collidePointCircle(mouseX, mouseY, 250, 900, 100) and mousePressed:
        theLine["red"] = 255
        theLine["green"] = 0
        theLine["blue"] = 0
    
    fill(0,0,255)  # blue
    stroke(color(0,0,0))
    ellipse(400, 900, 100, 100)
    if collidePointCircle(mouseX, mouseY, 400, 900, 100) and mousePressed:
        theLine["red"] = 0
        theLine["green"] = 0
        theLine["blue"] = 255
    
    fill(150,0,255)  # purple
    stroke(color(0,0,0))
    ellipse(550, 900, 100, 100)
    if collidePointCircle(mouseX, mouseY, 550, 900, 100) and mousePressed:
        theLine["red"] = 150
        theLine["green"] = 0
        theLine["blue"] = 255
    
    fill(255,150,0)  # orange
    stroke(color(0,0,0))
    ellipse(700, 900, 100, 100)
    if collidePointCircle(mouseX, mouseY, 700, 900, 100) and mousePressed:
        t

