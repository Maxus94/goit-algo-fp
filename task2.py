# import turtle

# def koch_curve(t, order, size):
#     if order == 0:        
#         t.forward(size)
#     else:
#         # for angle in [-30, 60]:
#         t.left(30)
#         koch_curve(t, order - 1, size * 0.7)
#         t.backward(size * 0.7)
#         # t.penup()
#         # t.goto(-size * 0.7 * ((2**0.5)/2), -(size * 0.7) / 2)
#         # t.pendown()        
#         t.right(30)
#         koch_curve(t, order - 1, size * 0.7)        
        

# def draw_koch_curve(order, size=300):
#     window = turtle.Screen()
#     window.bgcolor("white")

#     t = turtle.Turtle()
#     t.speed(0)  
#     t.penup()
#     t.goto(0, -size)
#     t.pendown()
#     t.left(90)

#     koch_curve(t, order, size)
#     # t.left(-120)
#     # koch_curve(t, order, size)
#     # t.left(-120)
#     # koch_curve(t, order, size)

#     window.mainloop()

# n = int(input("Введіть рівень рекурсії "))
# draw_koch_curve(n)


import turtle

 

def tree(branchLen,t):

    if branchLen > 5:

        t.forward(branchLen)

        t.right(20)

        tree(branchLen-15,t)

        t.left(40)

        tree(branchLen-15,t)

        t.right(20)

        t.backward(branchLen)

 

def main():

    t = turtle.Turtle()

    myWin = turtle.Screen()

    t.up()
    
    t.goto(0, -300)

    t.left(90)

    t.up()

    t.backward(100)

    t.down()

    t.color("green")

    tree(120,t)

    myWin.exitonclick()

 

main()