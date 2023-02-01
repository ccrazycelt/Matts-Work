"""
 Filename: bouncing_circle.py
 Author: 1352 instructors
 Date: January 2023
 Course: COMP 1352
 Assignment: animation demo, to be modified to use classes
 Collaborators: None
 Internet Source: None
"""

from random import random
import dudraw
from dudraw import Color
#self gets replaced with an instacne
class bouncing_ball:
    def __init__(self,x_position : float, y_position : float, x_velocity : float, y_velocity, radius):
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity= x_velocity
        self.y_velocity = y_velocity
        self.radius = radius
        self.color = Color(int(random()*256), int(random()*256), int(random()*256)) 
    def move(self):
        self.x_position += self.x_velocity
        self.y_position += self.y_velocity
        # bounce off the edges of the canvas if necessary:
        if (self.x_position > 1-self.radius and self.x_velocity > 0 or 
            self.x_position < self.radius and self.x_velocity < 0):
            self.x_velocity *= -1
        if (self.y_position > 1-self.radius and self.y_velocity > 0 or 
            self.y_position < self.radius and self.y_velocity < 0):
            self.y_velocity *= -1 
            
    def draw(self):
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.x_position, self.y_position, self.radius)
        dudraw.set_pen_color(self.color)
        dudraw.circle(self.x_position, self.y_position, self.radius)
    
    def overlaps(self, other):
        if (self.x_position-other.x_position)**2 + (self.y_position-other.y_position)**2 <= (self.radius+other.radius)**2 :
            self.color = Color(int(random()*256), int(random()*256), int(random()*256))
            other.color = Color(int(random()*256), int(random()*256), int(random()*256))
        
        
        
        

# main code block:
dudraw.set_canvas_size(1000,1000)

# create values to represent circle's properties

circle1 = bouncing_ball(random(),random(),0.2*random(), 0.2*random(), 0.4)
circle2 = bouncing_ball(random(),random(),0.2*random(), 0.2*random(), 0.05)

key = ''
while key != 'q':
    # redraw the frame:
    dudraw.clear(dudraw.LIGHT_GRAY)
    circle1.move()
    circle1.draw()
    circle2.move()
    circle2.draw()
    circle1.overlaps(circle2)
    # draw the circle at its new position
    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()

    # display the new frame and pause for 1/20 of a second
    dudraw.show(50)