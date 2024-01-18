# coding=utf-8
# Copyright (c) 2022 ichinae.com, Inc. All Rights Reserved
"""

Authors: sunjiale1023@ichinae.com
"""


class Television:
    def __init__(self):
        self.status = "off"
        self.current_channel = None

    def powerOn(self):
        if self.status == "off":
            self.status = "on"
            print("The television is now on.")
        else:
            print("The television is already on.")

    def powerOff(self):
        if self.status == "on":
            self.status = "off"
            print("The television is now off.")
        else:
            print("The television is already off.")

    def changeChannel(self, new_channel):
        if self.status == "on":
            self.current_channel = new_channel
            print(f"The channel has been changed to {self.current_channel}.")
        else:
            print("Please turn on the television before changing the channel.")

if __name__ == '__main__':
    television = Television()
    television.powerOn()