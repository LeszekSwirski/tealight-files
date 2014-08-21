from tealight.art import polygon
from math import sin, cos, pi





def triangle(x,y,size,angle=0):
  pts = []
  for i in range(0,4):
    theta = angle + i*2*pi/3
    pts.append((x + size*sin(theta),
                y + size*sin(theta)))
    
  print pts
  polygon(pts)
  
  
  
triangle(100,100,50)