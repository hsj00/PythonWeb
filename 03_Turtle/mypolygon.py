import turtle
bob = turtle.Turtle()
print(bob)


def square(length):
    for i in range(4):
        bob.fd(length)
        bob.lt(90)


print(square(200))

turtle.mainloop()
