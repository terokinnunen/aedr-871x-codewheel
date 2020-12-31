#!/usr/bin/env python3
import math
import svgwrite
from svgwrite import mm, cm

line_density = 12.52

cpr = 630
bar_length = 1.8


def wheel(name):
    wheel_circumference = 2 * cpr / line_density
    wheel_radius = wheel_circumference / (2 * math.pi)

    radius_inner = wheel_radius - bar_length / 2
    radius_outer = wheel_radius + bar_length / 2
    axel = radius_outer

    scale = 1
    pic_size = radius_outer * 2

    dwg = svgwrite.Drawing(
        filename=name, debug=True,
        size=(scale * pic_size * mm, scale * pic_size * mm))
    dwg.viewbox(0, 0, pic_size, pic_size)

    lines = dwg.add(dwg.g(id='lines', stroke='black'))

    def x(radius, index):
        return (axel + radius * math.cos(index * math.pi / cpr))

    def y(radius, index):
        return (axel + radius * math.sin(index * math.pi / cpr))

    def line(index):
        return dwg.polygon([
            (x(radius_inner, index), y(radius_inner, index)),
            (x(radius_outer, index), y(radius_outer, index)),
            (x(radius_outer, index+1), y(radius_outer, index+1)),
            (x(radius_inner, index+1), y(radius_inner, index+1)),
        ], stroke_width=0)
    # Last opaque not drawn = white index track
    for i in range(0, 2 * cpr - 2, 2):
        lines.add(line(i))
    # Black index track
    lines.add(line(2*cpr-17))

    dwg.save()


if __name__ == '__main__':
    wheel('wheel.svg')
