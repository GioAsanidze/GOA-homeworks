from turtle import*

#Homework is to create house with windows.
# getting the arrow to the position, where house will be in middle.

speed(20)
penup()
left(180)
forward(150)
left(90)
forward(300)
left(90)
pendown()

#drawing square for house.

color( "purple")
width(10)
forward( 300 )
left( 90 )
forward( 300 )
left( 90 )
forward( 300 )
left( 90 )
forward( 300 )
left(90)

#drawing the door.
#door size will be 90 in length and 130 in height.

forward(105)
color("yellow")
left(90)
forward(130)
right(90)
forward(90)
right(90)
forward(130)
left(90)

#now drawing the roof.
penup()
forward(105)
left(90)
forward(300)
pendown()
color("red")
begin_fill()
left(30)
forward(300)
left(120)
forward(300)
end_fill()
right(60)
#now it is time to draw windows.
#first i am going to get arrow in place where i want window to be.
#window will be 60 in lenght and 60 in height.
#just to be clear we started drawing house in coordinates (-150, -300 ).

penup()
goto(-60, -110)
width(5)
color("blue")
pendown()
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)

#now we draw second window exactly same as previous one.

penup()
goto(60, -110)
pendown()
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)

#and thats how we draw a house WITHOUT EVEN drawing.

exitonclick()