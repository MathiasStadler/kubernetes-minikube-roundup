# from here http://introtopython.org/classes.html


class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.

    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0

    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1


# Create a Rocket object.
my_rocket = Rocket()
print(my_rocket)
print (my_rocket.y)
my_rocket.move_up()
print (my_rocket.y)
