from manim import *

from .util import create_convolution_2d


class FinalScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(zoom=0.4)

        create_convolution_2d(self, [3, 5], 1, [3, 3], stride=2)
