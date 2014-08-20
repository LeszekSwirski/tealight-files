from tealight.art import *

c = [(100,20), (50,50), (200,300), (270, 50), (270, 400), (290,10)]
fill_polygon(c)

color("red")
#line(50,60,1000,60)
#spot(287.89,60,5)
print test_polygon(270,50,c)



for i in range(0,500,1):
  for j in range(0,500,1):
    if test_polygon(i,j,c):
      color("red")
    else:
      color("blue")
    spot(i,j,0.1)    