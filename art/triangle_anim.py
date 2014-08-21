from tealight.art import box,line_width,polygon,color,fill_polygon,clear,screen_width,screen_height
from math import sin, cos, pi, exp
from tealight.utils import sleep, now
from random import random

num_triangles = 40
max_size = max(min(screen_width, screen_height)/2. - 10, 10)
min_size = max_size / num_triangles
max_l = 95
min_l = 20

def make_triangle(x,y,size,angle=0):
  pts = []
  for i in range(0,3):
    theta = angle + i*2*pi/3
    pts.append((x + size*sin(theta),
                y + size*cos(theta)))
  return pts

start = now()
mouse_x = None
pulse_offset = [random()*2*pi for i in range(0, num_triangles)]

def draw():
  max_twist = 2*pi * 5. / num_triangles
  age = now() - start
  if mouse_x is not None:
    m_a = (mouse_x / float(screen_width) - 0.5)*2 * max_twist
  else:
    m_a = sin(age/2.) * max_twist * exp(-age/20)
  
  color("black")
  box(0,0,screen_width,screen_height)
  
  for i in range(0, num_triangles):
    size = min_size + (max_size - min_size) * float(i) / num_triangles
    size = max_size-size
    size *= (sin(age + pulse_offset[i])*0.1 + 1)
    
    l = min_l + (max_l - min_l) * float(i) / num_triangles
    
    tri = make_triangle(screen_width/2.,
                        screen_height/2.,
                        size,
                        i*m_a)
    color("hsl(230,100%," + str(round(l)) + "%)")
    fill_polygon(tri)
  
    color("hsl(230,100%," + str(round(l - 10)) + "%)")
    polygon(tri)
    
line_width(2)

def handle_mousedown(x,y):
  global mouse_x
  mouse_x = x

def handle_mousemove(x,y):
  global mouse_x
  if mouse_x is not None:
    mouse_x = x

def handle_mouseup():
  global start, mouse_x
  start = now()
  mouse_x = None

last_frame = 0
def handle_frame():
  global last_frame
  if now() - last_frame < 1./30.:
    #print "dropping frame"
    return
  
  draw()
  
  last_frame = now()
  sleep(1000./30. - 5)
