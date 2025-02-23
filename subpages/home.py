#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/24 11:59
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :

from streamlit import title, divider, expander, caption, empty
from streamlit_agraph import agraph, Node, Edge, Config

title("LangGraph")
divider()
with expander("Introduction", expanded=True):
    caption("This is the introduction page.")

empty_message: empty = empty()

nodes = [
    Node(id="start", label="Start", size=30, color="pink"),
    Node(id="Bob", label="Bob", size=25, color="blue"),
    Node(id="Charlie", label="Charlie", size=25, color="purple"),
]

edges = [
    Edge(source="Alice", target="Bob", label="朋友"),
    Edge(source="Bob", target="Charlie", label="同事"),
    Edge(source="Charlie", target="Alice", label="邻居"),
]

config = Config(width=800, height=500, physics=True, directed=False)

agraph(nodes=nodes, edges=edges, config=config)
