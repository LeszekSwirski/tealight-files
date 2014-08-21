from tealight.art import box,line_width,polygon,color,fill_polygon,clear,screen_width,screen_height
from math import sin, cos, pi
from tealight.utils import sleep, age

def make_triangle(x,y,size,angle=0):
  pts = []
  for i in range(0,3):
    theta = angle + i*2*pi/3
    pts.append((x + size*sin(theta),
                y + size*cos(theta)))
  return pts;
  

last_frame = 0

line_width(3)
def handle_frame():
  global last_frame
  if age() - last_frame < 1./30.:
    return
  
  m_a = sin(age()/1.) * 2*pi / 100.
  
  color("white")
  box(0,0,screen_width,screen_height)
  
  for i in range(1,25):
    tri = make_triangle(200,200,200-i*6,2*i*m_a)
    color("hsl(0,100%," + str(i*4) + "%)")
    fill_polygon(tri)
  
    color("hsl(0,100%," + str(i*4-20) + "%)")
    polygon(tri)
  
  last_frame = age()
  sleep(1000./10.)
    