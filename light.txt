# coding=utf-8
# Copyright (c) 2022 ichinae.com, Inc. All Rights Reserved
"""

Authors: sunjiale1023@ichinae.com
"""


class Light:
    def __init__(self):
        self.status = "off"

    def turnOn(self):
        self.status = "on"
        print("The light is now on.")

    def turnOff(self):
        self.status = "off"
        print("The light is now off.")

if __name__ == '__main__':
    light = Light()
    light.turnOn()