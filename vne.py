from manim import *


class Slide1(Scene):
    def construct(self):
        title = Text(
            "Meet Our Users – A Day in the Digital Life", font_size=30)
        self.play(Write(title))
        self.wait(1)

        users = [
            ("Sara", "Online Class", LEFT*3+UP),
            ("Alex", "Gaming", LEFT*3),
            ("Maya", "Streaming", LEFT*3+DOWN),
            ("Liam", "Remote Work", RIGHT*3+UP)
        ]

        icons = VGroup()
        for name, activity, position in users:
            icon = Circle(radius=0.4, color=BLUE).move_to(position)
            label = Text(f"{name}\n{activity}",
                         font_size=18).next_to(icon, RIGHT)
            icons.add(VGroup(icon, label))

        self.play(LaggedStart(*[FadeIn(i) for i in icons], lag_ratio=0.5))
        self.wait(2)

        message = Text(
            "Users expect seamless connectivity, low latency, and high-quality service.", font_size=20).to_edge(DOWN)
        self.play(Write(message))
        self.wait(2)


class Slide2(Scene):
    def construct(self):
        title = Text("From Users to Networks – Bridging the Gap", font_size=30)
        self.play(Write(title))
        self.wait(1)

        user_icons = [Circle(radius=0.3, color=GREEN).move_to(pos) for pos in [
            LEFT*5+UP, LEFT*5, LEFT*5+DOWN, LEFT*5+2*DOWN]]
        service_clouds = [Ellipse(width=1, height=0.5, color=YELLOW).move_to(
            icon.get_center()+RIGHT*3) for icon in user_icons]
        substrate_rect = Rectangle(
            width=6, height=3, color=GREY).move_to(RIGHT*3)
        substrate_label = Text("Physical Infrastructure", font_size=18).move_to(
            substrate_rect.get_center())

        # Step 1
        self.play(*[Create(icon) for icon in user_icons])
        self.wait(0.5)
        self.play(*[TransformFromCopy(user_icons[i], service_clouds[i])
                  for i in range(len(user_icons))])
        self.wait(1)

        # Step 2
        virtual_nodes = [Circle(radius=0.2, color=ORANGE).move_to(
            cloud.get_center()) for cloud in service_clouds]
        self.play(*[Transform(cloud, node)
                  for cloud, node in zip(service_clouds, virtual_nodes)])
        virtual_edges = VGroup(
            *[Line(node.get_center(), substrate_rect.get_center(), color=ORANGE) for node in virtual_nodes])
        self.play(Create(virtual_edges))
        self.wait(1)

        # Step 3
        self.play(Create(substrate_rect), Write(substrate_label))
        self.wait(1)

        message = Text(
            "User requests can be represented as virtual networks (graphs) embedded into physical infrastructure.", font_size=18).to_edge(DOWN)
        self.play(Write(message))
        self.wait(2)


class Slide3(Scene):
    def construct(self):
        title = Text(
            "The Challenge – The Virtual Network Embedding Puzzle", font_size=30)
        self.play(Write(title))
        self.wait(1)

        puzzle_substrate = Square(side_length=3, color=GREY).shift(LEFT*2)
        puzzle_virtual = [Polygon([-0.5, 0, 0], [0, 0.5, 0], [0.5, 0, 0], [
                                  0, -0.5, 0], color=BLUE).scale(0.7).shift(RIGHT*3+UP*i) for i in [1, 0, -1]]

        self.play(Create(puzzle_substrate))
        self.wait(0.5)
        self.play(LaggedStart(*[FadeIn(piece)
                  for piece in puzzle_virtual], lag_ratio=0.5))
        self.wait(1)

        arrows = VGroup(*[Arrow(piece.get_left(), puzzle_substrate.get_right())
                        for piece in puzzle_virtual])
        self.play(*[GrowArrow(arrow) for arrow in arrows])
        self.wait(1)

        questions = BulletedList(
            "Efficient resource allocation?",
            "Optimal placement for quality?",
            "Dynamic adaptability to evolving requests?",
            font_size=18
        ).to_edge(DOWN)

        self.play(Write(questions))
        self.wait(2)

        message = Text("Efficiently embedding virtual networks into physical resources defines the Virtual Network Embedding (VNE) problem.",
                       font_size=16).to_edge(DOWN, buff=0.2)
        self.play(Transform(questions, message))
        self.wait(2)
