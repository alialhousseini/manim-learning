from manim import *


class Intro(Scene):
    '''
    We start by creating a square and a circle, everything initally starts at center, therefore
    we shift them to the left and right respectively. Then we animate them to appear on screen. (Write)

    We want to move them up and down, so we animate them to move up and down.

    Now they are in their new positions, we rotate the square by 90 degrees and scale the circle by 2.
    In addition, we fill them with their respective colors with 80% opacity.

    We wait a bit, we change their colors to green and orange.
    And then, we turn them back to their original positions. (shift)

    Finally, we fade them out from the scene.
    '''

    def construct(self):
        # create square and circle objects (and move them)
        square = Square(color=RED).shift(LEFT * 2)
        # SAME AS
        # square = Square(color=RED)
        # square.shift(LEFT * 2)

        circle = Circle(color=BLUE).shift(RIGHT * 2)

        # animate writing them on screen
        self.play(Write(square), Write(circle))

        # moving objects using `animate`
        self.play(
            square.animate.shift(UP * 0.5),
            circle.animate.shift(DOWN * 0.5)
        )

        # rotating and filling the square (opacity 80%)
        # scaling and filling the circle (opacity 80%)
        self.play(
            square.animate.rotate(PI / 2).set_fill(RED, 0.8),
            circle.animate.scale(2).set_fill(BLUE, 0.8),
        )

        self.wait(1)

        # change color
        self.play(
            square.animate.set_color(GREEN),
            circle.animate.set_color(ORANGE),
        )

        # turn them back to original place
        self.play(
            square.animate.shift(DOWN * 0.5),
            circle.animate.shift(UP * 0.5),
        )

        # fading them from the scene
        self.play(FadeOut(square), FadeOut(circle), run_time=2)
