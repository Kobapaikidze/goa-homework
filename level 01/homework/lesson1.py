from turtle import*

width(7)
   
# we want to paint a house
color("black")
# step 1: draw a square
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
# end of square


#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)                          #height of thedoor
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,  200)
pendown()


color("black")
right(150)
forward(200)
left(120)
forward(200)
end_fill()


 #.end draw door
 
  #.  draw a window
        
penup()
        
        
goto(180,  180)             
pendown()        

color ("red") 

left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)




exitonclick()