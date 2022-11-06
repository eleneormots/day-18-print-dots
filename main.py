###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
#from turtle import Turtle
import random
import turtle

def get_colors():
    rgb_colors = []
    for _ in range (30):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        rgb_colors.append(color)
    return rgb_colors


def get_start_coordinates( dot_diameter, space_between_dots, num_rows, num_columns):
    painting_width= (dot_diameter+space_between_dots)* num_columns -space_between_dots
    painting_height=(dot_diameter+space_between_dots) * num_rows- space_between_dots
    start_x=(0-painting_width)/2
    start_y=(0-painting_height)/2
    return (start_x, start_y)

def paint_dots():
    dot_diameter = 20
    space_between_dots = 50
    num_rows=10
    num_columns=10
    turtle.colormode(255)
    color_list=get_colors()
    tim=turtle.Turtle()
    screen = turtle.Screen()
    start_coordinates=get_start_coordinates(dot_diameter, space_between_dots, num_rows, num_columns)
    pos_start_x= start_coordinates[0]
    pos_start_y=start_coordinates [1]
    for i in range(num_rows):
        tim.penup()
        tim.setposition(pos_start_x, pos_start_y)
        for j in range(num_columns):
            tim.pendown()
            tim.dot(dot_diameter, random.choice(color_list))
            tim.penup()
            if j != 9:
                tim.forward(space_between_dots)
        pos_start_y += space_between_dots
        if i!=9:
            tim.setposition(pos_start_x, pos_start_y)
    screen.exitonclick()

def main():
    paint_dots()

if __name__ == "__main__":
    main()

