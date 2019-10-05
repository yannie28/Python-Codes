#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

This program draws three
rectangles filled with different
colours.

Author: Jan Bodnar
Last modified: April 2019
Website: www.zetcode.com
"""

from tkinter import Tk, Canvas, Frame, BOTH
import time
class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Colours")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        listColor = ['#05f','#f50','#fc8eac','#05f','#f50']
        for i in range(3):
            canvas.create_rectangle(30, 10, 120, 80,
                outline=listColor[i], fill=listColor[i])
            canvas.create_rectangle(150, 10, 240, 80,
                outline=listColor[i+1], fill=listColor[i+1])
            canvas.create_rectangle(270, 10, 370, 80,
                outline=listColor[i+2], fill=listColor[i+2])
            canvas.pack(fill=BOTH, expand=1)

def main():

    root = Tk()
    Example()
    root.geometry("600x200+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()