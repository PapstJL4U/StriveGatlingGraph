#!/usr/bin/python3
# -*- coding: utf-8 -*-
import networkx as nx
from typing import Type, List
from Table import Table
from Moves import Moves
from DrawTable import DrawTable
import os

def Ino():

    attacks = ["5P", "6P", "2P", "5K", "2K", "c.S", "f.S", "2S", "5HS", "2HS", "6HS", "2D", "5D", "Jump", "Special"]
    attack_list : List[Moves]= []

    for attack in attacks:
        attack_list.append(Moves(name=attack))

    Ino_Table = Table(name="Ino", attack_list=attack_list)

    # standing normals
    p5 = ["5P", "5P", "2P", "6P", "6HS", "Special"]
    k5 = ["5K", "6P", "6HS", "2D", "5D", "Jump", "Special"]
    cS = ["c.S", "6P", "f.S", "2S", "5HS", "2HS", "6HS", "5D", "2D", "Jump", "Special"]
    fS = ["f.S", "5HS", "6HS", "Special"]
    p6 = ["6P", "Special"]
    hs6 = ["6HS", "Special"]
    hs5 = ["5HS", "Special"]

    # crouching normals
    p2 = ["2P", "5P", "2P", "6P", "6HS", "Special"]
    k2 = ["2K", "6P", "6HS", "5D", "2D", "Special"]
    s2 = ["2S", "5HS", "2HS", "Special"]
    d2 = ["2D", "Special"]
    hs2 = ["2HS", "Special"]

    table = [p5,k5, cS, fS, p6, hs6, hs5, p2, k2, s2, d2, hs2]

    for move in table:
        Ino_Table.add_multiple_gatlings(move)

    return Ino_Table

if __name__ == '__main__':

    test = Ino()
    test.printattacklist()
    for g in test.gatlings:
        print(g)

    newTable, width, height = DrawTable.generate_groups(table=test)
    image = DrawTable.generate_image(table=test, group= newTable, width=width, height=height)
    out = DrawTable.draw_button(image, 0, test.attack_list[0])
    I
    out.save(os.path.join("output", "test.png"))