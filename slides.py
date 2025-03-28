from manim import *
from manim_slides import Slide


class ThesisPresentation(Slide, MovingCameraScene):
    def construct(self):
        ####################################
        # Slide 1: Fade in the title
        ####################################
        title = Text("Explainable Reinforcement Learning for VNE")
        self.play(FadeIn(title))
        self.wait(1)
        self.next_slide()

        ####################################
        # Slide 2: Display words vertically on the left
        ####################################
        words = VGroup(
            Text("Explainable"),
            Text("Reinforcement Learning"),
            Text("VNE")
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT, buff=1)
        self.play(FadeIn(words, shift=LEFT))
        self.wait(1)
        self.next_slide()

        ####################################
        # Slide 3: Add each word inside a colored box
        ####################################
        # Create a surrounding rectangle (a "box") around each word.
        boxes = VGroup(*[
            SurroundingRectangle(word, color=BLUE, buff=0.3)
            for word in words
        ])
        self.play(Create(boxes))
        self.wait(1)
        self.next_slide()

        ####################################
        # Slide 4: Zoom in inside the first box ("Explainable")
        ####################################
        first_box = boxes[0]

        # Now, safely copy the camera frame.
        original_frame = self.camera.frame.copy()

        # Animate the camera to move and zoom in on the first box.
        self.play(
            self.camera.frame.animate
                .move_to(first_box.get_center())
                .set_width(first_box.width * 1.5)
        )
        self.wait(1)
        self.next_slide()

        ####################################
        # Slide 5: Inside the "Explainable" slide
        ####################################
        # Fade out the original "Explainable" text (that was part of the list)
        # and replace it with a centered title at the top.
        explainable_title = Text("Explainable").to_edge(UP)
        # Create a black box representing the “black box” in Explainable AI.
        black_box = Rectangle(
            width=2, height=2, fill_color=BLACK, fill_opacity=1)
        self.play(FadeOut(words[0]), FadeIn(explainable_title))
        self.wait(0.5)
        self.play(FadeIn(black_box))
        # (Optional) Animate the black box—for example, a slight rotation.
        self.play(Rotate(black_box, angle=PI/8))
        self.wait(1)
        self.next_slide()

        ####################################
        # Slide 6: Zoom out to the previous (Slide 3) view
        ####################################
        self.play(
            self.camera.frame.animate
                .move_to(original_frame.get_center())
                .set_width(original_frame.get_width())
        )
        self.wait(1)
        self.next_slide()

        ####################################
        # Slide 7: Zoom in to the next box ("Reinforcement Learning")
        ####################################
        second_box = boxes[1]
        self.play(
            self.camera.frame.animate
                .move_to(second_box.get_center())
                .set_width(second_box.width * 1.5)
        )
        self.wait(1)
        self.next_slide()

        ####################################
        # Slide 8: Explain Reinforcement Learning
        ####################################
        explanation_text = Text(
            "Reinforcement Learning:\nAn agent learns to make decisions\nthrough trial and error."
        ).to_edge(UP)
        self.play(FadeIn(explanation_text))
        self.wait(2)
        self.next_slide()

        # Optionally, zoom back out to the original full view.
        self.play(
            self.camera.frame.animate
                .move_to(original_frame.get_center())
                .set_width(original_frame.get_width())
        )
        self.wait(1)
