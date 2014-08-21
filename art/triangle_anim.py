from tealight.art import box,line_width,polygon,color,fill_polygon,clear,screen_width,screen_height
from math import sin, cos, pi
from tealight.utils import sleep, age

num_triangles = 60
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

def draw():
  m_a = sin(age()/2.) * 2*pi * 3. / num_triangles
  
  color("black")
  box(0,0,screen_width,screen_height)
  
  for i in range(0, num_triangles):
    size = min_size + (max_size - min_size) * float(i) / num_triangles
    l = min_l + (max_l - min_l) * float(i) / num_triangles
    
    tri = make_triangle(screen_width/2.,
                        screen_height/2.,
                        max_size-size,
                        i*m_a)
    color("hsl(230,100%," + str(round(l)) + "%)")
    fill_polygon(tri)
  
    color("hsl(230,100%," + str(round(l - 10)) + "%)")
    polygon(tri)
    
line_width(3)

last_frame = 0
def handle_frame():
  global last_frame
  if age() - last_frame < 1./30.:
    print "dropping frame"
    return
  
  draw()
  
  last_frame = age()
  sleep(1000./30.)
