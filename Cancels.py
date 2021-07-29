#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""the class represents grounded normals"""
import Moves


class Cancels(Moves):

    def __init__(self, name: str = "jump"):

        if name == "jump":
            Moves().__init__(name)
        elif name == "special":
            Moves().__init__(name)
        else:
            print("Unsupported Cancel: ", name)

