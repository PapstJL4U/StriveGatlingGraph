#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""the class represents grounded normals"""
import Moves


class Cancels(Moves):
    """Moves can be canceled into Jump or Special moves and need representation"""
    def __init__(self, name: str = "jump"):

        if name == "jump":
            Moves().__init__(name)
        elif name == "special":
            Moves().__init__(name)
        else:
            print("Unsupported Cancel: ", name)

