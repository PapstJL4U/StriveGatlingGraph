#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""this class represents a gatling table"""
from collections import defaultdict
from typing import Type
from Moves import Moves
from PIL import Image, ImageDraw, ImageFont, ImageColor
from Table import Table


class DrawTable:

    def generate_groups(table: Type[Table]):
        """returns a dictionary with the attacks grouped by style as well as
        dimensions in with largest group (width) and number of groups(height)"""

        print("generate groups")
        attack_list = table.attack_list
        width, height = 0, 0

        group = defaultdict(list)
        for attack in attack_list:
            group[attack.style].append(attack)
            w = len(group[attack.style])
            if w > width:
                width = w

        print(group)
        height = len(group)
        return group, width, height

    def draw_button(draw_instance, x_coord, move : Type[Moves]):

        draw = draw_instance
        x = x_coord
        col = ImageColor.getrgb(move.colour)
        draw.ellipse((x, x, x+200, x+200), fill=col, outline=(0, 0, 0))

    def generate_image(table, group, height, width):
        """generate an image"""
        icon_w, icon_h = 250, 250
        table_image = Image.new(mode="RGBA", size=(icon_w * width, height * icon_h))

