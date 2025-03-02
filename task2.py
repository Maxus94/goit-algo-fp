
import turtle

def tree(branchLen,t, level):

    if level > 0:
        t.forward(branchLen)
        t.right(30)
        tree(branchLen * 0.7, t, level-1)
        t.left(60)
        tree(branchLen * 0.7, t, level-1)
        t.right(30)
        t.backward(branchLen)        
 

def draw_tree(level):

    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.up()    
    t.goto(0, -300)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(300,t, level)
    myWin.exitonclick()

level = int(input("Enter tree levels: "))
draw_tree(level)