#!/usr/bin/env python

import Tkinter
from PIL import Image, ImageTk

class PersonLabeling(object):
    def __init__(self):
        self.top = Tkinter.Tk()
        self.top.title('PersonLabeling')
        
        self.image = Image.open('lena.jpg')
        self.image_widget = ImageTk.PhotoImage(self.image)
        self.label = Tkinter.Label(self.top, image = self.image_widget)
        self.label.pack()
        
        self.prev_btn = Tkinter.Button(self.top, text = 'Prev')
        self.next_btn = Tkinter.Button(self.top, text = 'Next')
        self.prev_btn.pack()
        self.next_btn.pack()
    
def main():
    obj = PersonLabeling()
    Tkinter.mainloop()

if __name__ == '__main__':
    main()
