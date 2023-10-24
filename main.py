import turtle
import tkinter as tk

high = 50
low = -50
sect = 25


def low2high(t):
    t.sety(low)
    t.pendown()
    t.forward(sect)
    t.sety(high)
    t.forward(sect)


def high2low(t):
    t.sety(high)
    t.pendown()
    t.forward(sect)
    t.sety(low)
    t.forward(sect)


def manchester(bits):
    root, t = setup("Manchester Encoding")

    for idx, x in enumerate(bits):
        if idx == 0:
            t.penup()

        if x == 0:
            high2low(t)
        elif x == 1:
            low2high(t)
        else:
            print("Wrong Input Value")
            break

    return root


def differentialManchester(bits):
    root, t = setup("Differential Manchester Encoding")
    # init pen setting
    t.penup()
    t.sety(high)
    t.pendown()

    # transition by previous state
    state = 1 if t.ycor() == high else -1
    mode = {1: low2high, -1: high2low}

    for idx, x in enumerate(bits):
        if x == 0:
            if idx == 0:
                t.sety(low)
            mode[state](t)
        elif x == 1:
            state *= -1
            mode[state](t)
        else:
            print("Wrong Input Value")
            break

    return root


def setup(title):
    root = tk.Tk()
    root.title(title)
    root.geometry('1000x150')
    root.resizable(True, False)

    cv = tk.Canvas(root, width=1000, height=140)
    cv.pack()
    sc = turtle.TurtleScreen(cv)

    t = turtle.RawTurtle(sc)
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(-500,0)
    t.pendown()

    return root, t


bits = list(map(int, input("Input bits: ")))
w1 = manchester(bits)
w2 = differentialManchester(bits)
w1.mainloop()
w2.mainloop()
