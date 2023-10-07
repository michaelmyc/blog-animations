from manim import *

from .util import create_array


class FinalScene(Scene):
    def construct(self):
        scale = 0.75
        array = create_array([3, 5], padding=1, scale=scale)
        kernel = create_array([3, 3], scale=scale, color=ORANGE)
        array.generate_target()
        kernel.generate_target()
        array.target.set_y(-1.5)
        kernel.target.set_y(2)
        self.add(array)
        self.add(kernel)

        self.play(MoveToTarget(array), MoveToTarget(kernel))

        # group[3].set_color(RED)
        # group[3].set_fill(RED)
        # group[3].set_z_index(999)

        # print(group.get_center())
        # print(group[0].get_center())
        # group.move_to([-2, -2, 0])
