from tealight.art import line_width,polygon,color,fill_polygon,clear
from math import sin, cos, pi
from tealight.utils import sleep



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
  

m_a = 0

line_width(3)
def handle_frame():
  global m_a
  
  for i in range(0,50):
    color("hsl(0,100%," + str(i*2) + "%)")
    fill_triangle(200,200,200-i*2,i*m_a)
  
    color("hsl(0,100%," + str(i*2-20) + "%)")
    triangle(200,200,200-i*2,i*m_a)
    
  m_a += 0.01
  
  sleep(10)
    