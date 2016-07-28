#!/usr/bin/env python

from Tkinter import *
from PIL import Image, ImageTk, ImageDraw

class PersonLabeling(object):
    def __init__(self):
        self.top = Tk()
        self.top.title('PersonLabeling')
        
        self.image = Image.open('test.jpg')
        self.image_widget = ImageTk.PhotoImage(self.image)

        self.label = Label(self.top, image = self.image_widget)
        self.label.bind('<Button-1>', self.image_click)
        self.label.bind('<ButtonRelease-1>',self.image_click_release)
        self.label.pack()

        self.prev_btn = Button(self.top, text = 'Prev')
        self.next_btn = Button(self.top, text = 'Next')
        self.clean_btn = Button(self.top, text = 'Clean')
        self.prev_btn.pack(side=LEFT)
        self.next_btn.pack(side=RIGHT)
        self.clean_btn.pack()
        self.prev_btn.bind('<Button-1>',self.click)
        self.next_btn.bind('<Button-1>',self.click)


    def image_click(self, event):
        self.start_x = event.x
        self.start_y = event.y
        print event.x,event.y

    def image_click_release(self, event):
        draw = ImageDraw.Draw(self.image)
        draw.rectangle([(self.start_x,self.start_y),(event.x,event.y)], outline = (255,0,0))
        del draw
        self.image_widget = ImageTk.PhotoImage(self.image)
        self.label.configure(image = self.image_widget)
        print event.x,event.y

    def click(self, event):
        psss

    def clean_label_info(self, event):
        pass
    
def main():
    obj = PersonLabeling()
    mainloop()

if __name__ == '__main__':
    main()
