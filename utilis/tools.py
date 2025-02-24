#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/24 12:27
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   tools.py
# @Desc     :   

from enum import unique, StrEnum

from streamlit import sidebar, header, slider, selectbox, caption


@unique
class Colour(StrEnum):
    """ Color Enum """
    RED = "#FFAAAA"
    YELLOW = "#FFEEAA"
    BLUE = "#88EEFE"
    GREEN = "#AAFFAA"
    GRAY = "#525352"


@unique
class Shape(StrEnum):
    # IMAGE: str = "image"
    # CIRCULAR_IMAGE: str = "circularImage"
    DIAMOND: str = "diamond"
    DOT: str = "dot"
    STAR: str = "star"
    TRIANGLE: str = "triangle"
    TRIANGLE_DOWN: str = "triangleDown"
    HEXAGON: str = "hexagon"
    SQUARE: str = "square"


def params_flowchart():
    with sidebar:
        header("Flowchart Parameters")

        options_colour = [colour.value for colour in Colour]
        node_colour: str = selectbox("Node Colour", options_colour, index=1,
                                     placeholder="Choose an option",
                                     help="Select the Node Color")
        caption(f"The selected colour is {node_colour}")

        options_shape = [shape.value for shape in Shape]
        node_shape: str = selectbox("Node Shape", options_shape, index=6,
                                    placeholder="Choose an option",
                                    help="Select the Node Shape")
        caption(f"The selected shape is {node_shape}")

        node_size: int = slider("Node Size", 20, 35, 25, 1, format="%d", help="Slide to change the Node Size")
        caption(f"The selected size is {node_size}")

        font_size: int = slider("Font Size", 12, 24, 14, 1, format="%d", help="Slide to change the Font Size")
        caption(f"The selected size is {font_size}")

        edge_width: int = slider("Edge Width", 1, 10, 3, 1, format="%d", help="Slide to change the Edge Width")
        caption(f"The selected width is {edge_width}")

        edge_colour: str = selectbox("Edge Colour", options_colour, index=4,
                                     placeholder="Choose an option",
                                     help="Select the Edge Color")
        caption(f"The selected colour is {edge_colour}")

        options_style = ["solid", "dashed", "dotted"]
        style: str = selectbox("Edge Style", options_style, index=0,
                               placeholder="Choose an option",
                               help="Select the Edge Style")
        caption(f"The selected style is {style}")
        match style:
            case "solid":
                edge_style = False
            case "dashed":
                edge_style = [5, 5]
            case "dotted":
                edge_style = [1, 5]

        return node_colour, node_shape, node_size, font_size, edge_width, edge_colour, edge_style
