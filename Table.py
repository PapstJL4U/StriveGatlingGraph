#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""this class represents a gatling table"""
from typing import Type, List, Iterable
from Moves import Moves


class Table(object):
    """This class represents the complete gatling table with moves and gattlings."""

    def __init__(self, name: str, attack_list: Iterable[Moves]):
        self._name = name
        self._attack_list = attack_list
        self._gatlings: [str] = []

    @property
    def name(self):
        "should be the name of the character"
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def attack_list(self) -> Iterable[Moves]:
        "List of attacks"
        return self._attack_list

    @attack_list.setter
    def attack_list(self, value: Iterable[Moves]):
        self._attack_list = value

    def printattacklist(self):
        print("Grounded Normals:")
        for attack in self._attack_list:
            print(str(attack) + " ", end='')
        print("- END")

    @property
    def gatlings(self):
        "returns all possible gatlings"
        return self._gatlings

    @gatlings.setter
    def gatlings(self, value):
        self._gatlings = value

    def add_single_gatling(self, gatling: Iterable[str]):
        """Add a single gatling by adding the starting and a follow up attack"""
        button = gatling[0].upper()
        gat = gatling[1]
        attacks_as_str = self._attack_list_as_str_list()
        if button in attacks_as_str:
            combo = self._find_button_gatling(button)
            combo.append(gat)
        else:
            print("Button not part of character set: ", button)
            self.printattacklist()

    def add_multiple_gatlings(self, gatlings: Iterable[str]):
        """add multiple gatlings, that all start from the same button"""
        # example: 5P->5P, 5P->6P, 5P->6HS
        # gatlings = ["5P", "5P", "6P", "6HS"]
        # the gatlings[0] must always be the start button
        button = gatlings[0].upper()
        gatl = gatlings[1:]
        attacks_as_str = self._attack_list_as_str_list()
        if button in attacks_as_str:
            combo = self._find_button_gatling(button)
            for g in gatl:
                combo.append(g)
        else:
            print("Button not part of character set: ", button)
            self.printattacklist()

    def _find_button_gatling(self, button: str) -> list:

        gat = []
        for gatling in self._gatlings:
            if gatling[0] == button:
                gat = gatling
                break

        if len(gat) == 0:
            gat = [button]
            self._gatlings.append(gat)
            return gat
        else:
            return gat

    def _attack_list_as_str_list(self) -> List[str]:

        str_lst = []
        for move in self._attack_list:
            str_lst.append(move.name)
        return str_lst