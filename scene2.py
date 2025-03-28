from manim import *


class Intro(Scene):
    '''
    Sometimes we want to move an obj in relation to other objs in the scene.
    We can use the next_to function to move an object in relation to another object.

    In this example, we create 4 circles and a rectangle. We move the circles such that they surround the rectangle.

    '''

    def construct(self):
        ####################################
        # next_to: move an object in relation to other objects in the scene
        c1, c2, c3, c4 = [Circle(radius=0.5, color=WHITE)
                          for _ in range(4)]

        rectangle = Rectangle(width=5, height=3)

        # use Python's * syntax to write the objects
        # does the following: f(*[1, 2, 3]) == f(1, 2, 3)

        # instead of Write, we use FadeIn to animate the objects
        self.play(*[FadeIn(o)
                  for o in [c1, c2, c3, c4, rectangle]])

        self.wait(1)

        # move the circles such that they surround the rectangle
        self.play(
            c1.animate.next_to(rectangle, LEFT),
            c2.animate.next_to(rectangle, UP),
            c3.animate.next_to(rectangle, RIGHT),
            c4.animate.next_to(rectangle, DOWN),
        )

        self.wait(1)
