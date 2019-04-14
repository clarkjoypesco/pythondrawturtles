import turtle

def draw_square(some_turtle):

    for j in range(1,60):
        for i in range(1,5):
            some_turtle.forward(100)
            some_turtle.right(90)
        some_turtle.right(10)
        


def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')

    # Create the turtle coco
    coco = turtle.Turtle()
    coco.shape('turtle')
    coco.color('yellow')
    coco.speed(2)
    draw_square(coco)

    # nana = turtle.Turtle()
    # nana.shape('arrow')
    # nana.color('blue')
    # nana.circle(100)

    window.exitonclick()

draw_art()
