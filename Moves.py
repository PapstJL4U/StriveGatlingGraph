#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""the class represents grounded normals"""
from typing import List

class Moves(object):

    __styles = ["punch", "kick", "slash", "heavy slash", "dust"]

    def __init__(self, name: str = "5P", **kwargs):
        self._name = name.upper()
        if kwargs.get("style") == None:
            self._find_my_style(self._name)
        else:
            self._style = kwargs.get("style")
        self._startup = kwargs.get("startup")
        self._active = kwargs.get("active")
        self._recovery = kwargs.get("recovery")

    @classmethod
    def get_possible_attack_styles(self) -> List[str]:
        return self.__styles

    def attack_data(self, style: str, startup: int, active: int, recovery: int):

        self._style = style
        self._startup = startup
        self._active = active
        self._recovery = recovery


    def _find_my_style(self, name: str):

        if "jump" in name.lower():
            self._style = "extra"
        elif "special" in name.lower():
            self._style = "extra"
        elif "p" in name.lower():
            self._style = "punch"
        elif "k" in name.lower():
            self._style = "kick"
        elif "hs" in name.lower():
            self._style = "heavy slash"
        elif "d" in name.lower():
            self._style = "dust"
        else:
            if "s" in name.lower() and not "h" in name.lower():
                self._style = "slash"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.upper()

    @property
    def style(self) -> str:
        return self._style

    @style.setter
    def style(self, value: str):
        styles = self.__styles
        if value in styles:
            self._style = value
        else:
            print("Invalid type data: ", str(value))
            print("Trying to autocorrect based on ", self._name)
            self._find_my_style(self._name)


    @property
    def startup(self) -> int:
        return self._startup

    @startup.setter
    def startup(self, value: int):
        if value >= 0 and value <= 10000:
            self._startup = value
        else:
            self._startup = 0
            print("Invalid startup value: ", str(value))

    @property
    def active(self) -> int:
        return self._active

    @active.setter
    def active(self, value: int):
        if value >= 0 and value <= 10000:
            self._active = value
        else:
            self._active = 0
            print("Invalid active value: ", str(value))

    @property
    def recovery(self) -> int:
        return self._recovery

    @recovery.setter
    def recovery(self, value: int):
        if value >= 0 and value <= 10000:
            self._recovery= value
        else:
            self._recovery = 0
            print("Invalid recovery value: ", str(value))

    def __str__(self) -> str:
        return self._name

    @property
    def colour(self, htmlcode: bool = False) -> str:

        if self._style == None:
            self._find_my_style(self.name)

        colour = "ffffff"

        if self._style == "punch":
            if htmlcode:
                colour = "ff6781"
            else:
                colour = "pink"
        elif self._style == "kick":
            if htmlcode:
                colour = "3a00eb"
            else:
                colour = "blue"
        elif self._style == "slash":
            if htmlcode:
                colour = "007621"
            else:
                colour = "green"
        elif self._style == "heavy slash":
            if htmlcode:
                colour = "cd2000"
            else:
                colour = "red"
        elif self._style == "dust":
            if htmlcode:
                colour = "db7d00"
            else:
                colour = "orange"
        elif self._style == "extra":
            if htmlcode:
                colour = "663399"
            else:
                colour = "royal purple"
        return colour

    def __repr__(self):

        if self._startup == None:
            value = "Name:"+self._name
        else:
            value = "Name:"+ self._name + " "+str(self.startup)+"/"+str(self.active)+"/"+str(self.recovery)
        return value