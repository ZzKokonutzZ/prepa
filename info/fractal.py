import turtle
turtle.tracer(0)
def koch(a,size) :
    if a>0 :
        koch(a-1,size/3)
        turtle.right(60)
        koch(a-1,size/3)
        turtle.left(120)
        koch(a-1,size/3)
        turtle.right(60)
        koch(a-1,size/3)
        
    else :
        turtle.forward(size)
# koch(10,600)
# turtle.left(120)
# koch(10,600)
# turtle.left(120)
# koch(10,600)

def dragon(n,size) :
    if n==0 :
        turtle.forward(size)
    else :
        dragon(n-1,size)
        turtle.left(90)
        invdragon(n-1,size)

def invdragon(n,size) :
    if n==0 :
        turtle.forward(size)
    else :
        dragon(n-1,size)
        turtle.right(90)
        invdragon(n-1,size)

def pseudokoch(a,size) :
    if a>0 :
        pseudokoch(a-1,size/2)
        turtle.right(90)
        pseudokoch(a-1,size/2)
        turtle.left(90)
        pseudokoch(a-1,size/2)
        turtle.left(90)
        pseudokoch(a-1,size/2)
        turtle.right(90)
        pseudokoch(a-1,size/2)
    else :
        turtle.forward(size)

def sierpinsky(n,size) :
    if n>0 :
        for _ in range(3) :
            turtle.left(120)
            turtle.forward(size/2)
            sierpinsky(n-1,size/2)
            turtle.forward(size/2)
            
sierpinsky(5,100)

turtle.update()
turtle.exitonclick()