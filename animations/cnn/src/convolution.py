from manim import *

from .util import create_convolution_2d


class FinalScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(zoom=0.75)

        create_convolution_2d(self, [3, 5], 1, [3, 3], result_pos=[4.5, 0], stride=2)
