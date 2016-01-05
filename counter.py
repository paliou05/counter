# -*-coding: utf8-*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from datetime import datetime
import sys


if sys.version_info[0] < 3:
    input = raw_input
class TimeCounter(object):
    def __init__(self):
        self.start_time = None
    def start(self):
        self.start_time = datetime.now()
    @property
    def value(self):
        return (datetime.now() - self.start_time).total_seconds()
    def peek(self):
        return self.value
    def finish(self):
        return self.value
    def menu_result_1(self):
        raw_input("To start timing press enter")
        self.start()
        print ("Counting...")
        raw_input("Press enter to stop counting")
        seconds = self.finish()
        time = format(seconds)
        print (time)
    def menu_result_2(self):
        raw_input("To start press enter\n")
        self.start()
        print ("running...\n")
        while True:
            swoption = raw_input("To pause press (1)\nTo start again press (2)\nTo stop press (3)\n>")
            if swoption == "1":
                seconds = self.finish()
                time = format(seconds)
                time1= time
                print (time)
            elif swoption == "2":
                self.start()
                raw_input("To stop press enter\n")
                stopwatch = self.finish()
                time2 = format(stopwatch)
                time = float(time1) + float(time2)
                print (time)
            elif swoption == "3":
                break
                
if __name__=='__main__':
    timer = TimeCounter()
    while True:
        playermenumain = raw_input("What would you like to do?\n (1)Timer\n (2)Stopwatch\n (3)Exit\n>")
        if playermenumain == "1":
            timer.menu_result_1()
        elif playermenumain == "2":
            timer.menu_result_2()
        elif playermenumain == "3":
            break

