from numbers import Number

import numpy as np
from manim import *

# def create_convolution(
#     scene,
#     array_shape,
#     array_padding,
#     kernel_shape,
#     kernel_pos=[0, 2],
#     array_pos=[0, 0],
#     stride=[1, 1],
#     scale=1,
# ):
#     array = create_array(array_shape, padding=array_padding, pos=array_pos, scale=scale)
#     kernel = create_array(kernel_shape, color=ORANGE, pos=kernel_pos, scale=scale)
#     kernel.generate_target()
#     scene.add(array)
#     scene.add(kernel)
#     # for
#     kernel.target.set_x(0)
#     kernel.target.set_y(0)
#     scene.play(MoveToTarget(kernel))
#     kernel.target.set_x(1)
#     scene.play(MoveToTarget(kernel))


def create_array(
    shape,
    color=BLUE,
    padding_color=DARK_GREY,
    padding=[0, 0],
    opacity=0.2,
    pos=[0, 0],
    scale=1,
):
    squares = []
    paddings = []
    padded_shape = np.array(shape) + np.array(padding) * 2
    if isinstance(shape, Number):
        shape = [1, shape]
    if isinstance(padding, Number):
        padding = [padding, padding]
    for i in range(np.prod(padded_shape)):
        r = i // padded_shape[1]
        c = i % padded_shape[1]
        is_padding = False
        if (
            r < padding[0]
            or r >= padding[0] + shape[0]
            or c < padding[1]
            or c >= padding[1] + shape[1]
        ):
            is_padding = True
        square = Square(scale)
        if is_padding:
            square.set_z_index(-1)
            square.set_color(padding_color)
            square.set_fill(padding_color, opacity=opacity, family=False)
        else:
            square.set_color(color)
            square.set_fill(color, opacity=opacity, family=False)
        squares.append(square)
        paddings.append(is_padding)
    group = VGroup(*squares)
    group.arrange_in_grid(*padded_shape, buff=0)
    return group
