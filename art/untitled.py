from tealight.art import fill_polygon
from math import sin, cos, pi





def triangle(x,y,size):
  x0 = sin(0)
  y0 = cos(0)
  x1 = sin(2*pi/3)
  y1 = cos(2*pi/3)
  x2 = sin(2* 2*pi/3)
  y2 = cos(2* 2*pi/3)
  
  fill_polygon([(x0,y0),(x1,y1),(x2,y2)])
  
  
  
triangle(50,50,50)