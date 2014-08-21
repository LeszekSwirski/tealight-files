from tealight.art import polygon
from math import sin, cos, pi





def triangle(x,y,size,angle=0):
  pts = []
  for i in range(0,3):
    theta = angle + i*2*pi/3
    pts.append((x + size*sin(theta),
                y + size*sin(theta)))
    
  print pts
  polygon([(100.0, 100.0), (143.301270189, 143.301270189), (56.6987298108, 56.6987298108)])
  
  
  
triangle(100,100,50)