#!/usr/bin/python3
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

def INO():
    ino = nx.DiGraph(character="ino")
    ino.add_nodes_from(["5P","6P", "2P", "5K", "2K", "c.S", "f.S", "2S", "5HS", "2HS", "6HS", "2D", "5D", "Jump", "Special"])

    #standing normals
    ino.add_edges_from([("5P", "5P"), ("5P", "2P"), ("5P", "6P"), ("5P", "6HS"), ("5P", "Special")])
    ino.add_edges_from([("5K", "6P"), ("5K", "6HS"),("5K", "5D"),("5K", "2D"), ("5K", "Jump"), ("5K", "Special")])
    ino.add_edges_from([("c.S", "6P"),("c.S", "f.S"),("c.S", "2S"),("c.S", "5HS"),("c.S", "2HS"),
                        ("c.S", "6HS"),("c.S", "5D"),("c.S", "2D"),("c.S", "Jump"), ("c.S", "Special")])
    ino.add_edges_from([("f.S", "5HS"),("f.S", "6HS"),("f.S", "Special")])
    ino.add_edges_from([("6P", "Special")])
    ino.add_edges_from([("6HS", "Special")])
    ino.add_edges_from([("5HS", "Special")])

    #crouching normals
    ino.add_edges_from([("2P", "5P"), ("2P", "2P"), ("2P", "6P"), ("2P", "6HS"), ("2P", "Special")])
    ino.add_edges_from([("2K", "6P"), ("2K", "6HS"), ("2K", "5D"), ("2K", "2D"), ("2K", "Special")])
    ino.add_edges_from([("2S", "5HS"), ("2S", "2HS"), ("2S", "Special")])
    ino.add_edges_from([("2D", "Special")])
    ino.add_edges_from([("2HS", "Special")])

    return ino

if __name__ == '__main__':
    ino = INO()
    print(list(ino.nodes))
    nx.draw_circular(ino, with_labels=True, font_weight='bold')
    #pos = nx.multipartite_layout(ino)
    #nx.draw_networkx(ino, pos)
    plt.show()
    #plt.subplot(122)
   # nx.draw_shell(ino, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

