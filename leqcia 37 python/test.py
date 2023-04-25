from turtle import *
import colorsys

speed('fastest')
bgcolor('black')
width(3)
h = 0.0
for i in range(1250):
    col = colorsys.hsv_to_rgb(h,1,1)
    color(col)
    forward(i*10)
    right(121)
    h += 0.001
done()