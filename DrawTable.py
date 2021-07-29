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

    def draw_button(draw_instance, x_coord, move: Type[Moves]):

        col = ImageColor.getrgb(move.colour)
        x = x_coord

        btn = Image.new("RGBA", [100,100], (255, 255, 255, 0))
        fnt = ImageFont.truetype(r'C:\Windows\Fonts\chintzy.ttf', 60)
        txt_layer = ImageDraw.Draw(btn)
        txt_layer.ellipse([(x, x), (x + 100, x + 100)], fill=col, outline=(0, 0, 0))
        txt_layer.text((x + 12, x + 27), str(move.name), fill=(0, 0, 0, 255), font=fnt)

        btn.show()
        return btn

    def generate_image(table, group, width, height):
        """generate an image"""
        icon_w, icon_h = 250, 250
        table_image = Image.new(mode="RGBA", size=(icon_w * width, height * icon_h))
        return table_image
