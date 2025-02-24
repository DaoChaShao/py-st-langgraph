#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/24 11:59
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :

from streamlit import title, divider, expander, caption, empty
from streamlit_agraph import agraph, Node, Edge, Config

from utilis.tools import params_flowchart

title("LangGraph")
divider()
with expander("Introduction", expanded=True):
    caption("This is the introduction page.")

empty_message: empty = empty()

node_colour, node_shape, node_size, font_size, edge_width, edge_colour, edge_style = params_flowchart()

nodes = [
    Node(id="Start", label="Start", color=node_colour, shape=node_shape, size=node_size, font={"size": font_size}),
    Node(id="Agent", label="Agent", color=node_colour, shape=node_shape, size=node_size, font={"size": font_size}),
    Node(id="Tools", label="Tools", color=node_colour, shape=node_shape, size=node_size, font={"size": font_size}),
    Node(id="End", label="End", color=node_colour, shape=node_shape, size=node_size, font={"size": font_size}),
]

edges = [
    Edge(source="Start", target="Agent", arrow_to=True, width=edge_width, color=edge_colour, dashes=edge_style),
    Edge(source="Agent", target="Tools", arrow_to=True, width=edge_width, color=edge_colour, dashes=edge_style),
    Edge(source="Tools", target="Agent", arrow_to=True, width=edge_width, color=edge_colour, dashes=edge_style),
    Edge(source="Agent", target="End", arrow_to=True, width=edge_width, color=edge_colour, dashes=edge_style),
]

config = Config(physics=True, directed=True, hierarchical=True, fit=True)

agraph(nodes=nodes, edges=edges, config=config)
