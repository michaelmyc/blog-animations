from numbers import Number

import numpy as np
from manim import *


def create_convolution_2d(
    scene,
    array_shape,
    array_padding,
    kernel_shape,
    array_pos=[-4, 0],
    result_pos=[4, 0],
    stride=[1, 1],
    end_wait=1.5,
):
    if isinstance(array_shape, Number):
        array_shape = [1, array_shape]
    if isinstance(kernel_shape, Number):
        kernel_shape = [1, kernel_shape]
    if isinstance(array_padding, Number):
        array_padding = [array_padding, array_padding]
    if isinstance(stride, Number):
        stride = [stride, stride]

    array_shape = np.array(array_shape)
    array_padding = np.array(array_padding)
    kernel_shape = np.array(kernel_shape)
    array_pos = np.array(array_pos)
    result_pos = np.array(result_pos)
    stride = np.array(stride)

    padded_shape = array_shape + array_padding * 2
    result_shape = np.ceil((padded_shape - kernel_shape + 1) / stride).astype(int)
    conv_start = np.flip(array_pos) - (padded_shape / 2 - kernel_shape / 2) * [-1, 1]

    array = create_array_2d(array_shape, padding=array_padding, pos=array_pos)
    kernel = create_array_2d(kernel_shape, color=ORANGE, pos=np.flip(conv_start))
    kernel.set_z_index(999)
    kernel.generate_target()
    scene.add(array)
    scene.add(kernel)

    for r in range(result_shape[0]):
        for c in range(result_shape[1]):
            kernel.target.set_x(conv_start[1] + c * stride[1])
            kernel.target.set_y(conv_start[0] - r * stride[0])

            scene.play(MoveToTarget(kernel), run_time=0.5)

            part_result_pos = result_pos - np.flip(result_shape - 1) / 2 * [1, -1] + [c, -r]
            result = create_array_2d(1, GREEN, pos=part_result_pos)

            temp_kernel = kernel.copy()
            temp_kernel.set_z_index(1)
            scene.play(Transform(temp_kernel, result))

    scene.wait(end_wait)

    kernel.target.set_x(conv_start[1])
    kernel.target.set_y(conv_start[0])

    scene.play(MoveToTarget(kernel), run_time=0.5)

def create_array_2d(
    shape,
    color=BLUE,
    padding_color=DARK_GREY,
    padding=[0, 0],
    opacity=0.2,
    pos=[0, 0],
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
        square = Square(1)
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
    group.set_x(pos[0])
    group.set_y(pos[1])
    return group
