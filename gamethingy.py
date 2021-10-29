import turtle as trtl
import random as rand


tr = trtl.Turtle()
wn = trtl.Screen()
wn.bgpic("catbs.gif")
wn.addshape('catbs.gif')
tr.shape('catbs.gif')

spotColor = "Green"
spotShape = "catbs.gif"
spotSize = .1
score = 0

spot = trtl.Turtle()
spot.shape(spotShape)
spot.turtlesize(spotSize)
spot.fillcolor(spotColor)

spot.penup()

def spot_clicked(x,y):
  print(score)
  change_position()


def change_position():
  new_xpos = rand.randint(-180,180)
  new_ypos = rand.randint(-140,140)
  spot.hideturtle()
  spot.goto(new_xpos,new_ypos)
  spot.showturtle()
  
spot.onclick(spot_clicked)
  
  
wn = trtl.Screen()
wn.mainloop()