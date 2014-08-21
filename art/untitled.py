from tealight.art import line_width,polygon,color,fill_polygon
from math import sin, cos, pi





def triangle(x,y,size,angle=0):
  pts = []
  for i in range(0,3):
    theta = angle + i*2*pi/3
    pts.append((x + size*sin(theta),
                y + size*cos(theta)))
    
  polygon(pts)

def fill_triangle(x,y,size,angle=0):
  pts = []
  for i in range(0,3):
    theta = angle + i*2*pi/3
    pts.append((x + size*sin(theta),
                y + size*cos(theta)))
    
  fill_polygon(pts)
  
  

for i in range(0,50):
  color("hsl(0,100%," + str(i*2) + "%)")
  triangle(200,200,200-i*2,i*0.5)
  color("hsl(0,100%," + str(i*2) + "%)")
  triangle(200,200,200-i*2,i*0.5)