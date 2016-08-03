#!/usr/bin/env python

from Tkinter import *
from PIL import Image, ImageTk, ImageDraw
from utils import ProcessImages

class APP(object):
    def __init__(self):
        self.top = Tk()
        self.top.title('PersonLabeling')
        
        #  self.image = Image.open('test.jpg')
        self.processimages = ProcessImages.ProcessImages('images')
        self.images = self.processimages.GetImageList()
        self.images_info = dict().fromkeys(self.images,[])
        self.curImageIdx = 0

        self.label = Label(self.top)
        self.show_image(self.curImageIdx)

        self.label.bind('<Button-1>', self.image_click)
        self.label.bind('<ButtonRelease-1>',self.image_click_release)
        self.label.pack()

        self.prev_btn = Button(self.top, text = 'Prev')
        self.next_btn = Button(self.top, text = 'Next')
        self.clean_btn = Button(self.top, text = 'Clean')
        self.prev_btn.pack(side=LEFT)
        self.next_btn.pack(side=RIGHT)
        self.clean_btn.pack()
        self.prev_btn.bind('<Button-1>',self.prev_click)
        self.next_btn.bind('<Button-1>',self.next_click)

    def show_image(self,image_idx):
        self.image_widget = ImageTk.PhotoImage(Image.open(self.images[image_idx]))
        self.label.configure(image = self.image_widget)

    def image_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def image_click_release(self, event):
        self.save_image_info(self.curImageIdx,self.start_x,self.start_y,event.x,event.y,0,0)
        self.draw_image(self.curImageIdx)
    
    def draw_image(self,imgIdx): 
        drawnImage = Image.open(self.images[imgIdx])
        draw = ImageDraw.Draw(drawnImage)
        for x1,y1,x2,y2,age,gender in self.images_info[self.images[imgIdx]]:
            draw.rectangle([(x1,y1),(x2,y2)], outline = (255,0,0))
        del draw
        self.image_widget = ImageTk.PhotoImage(drawnImage)
        self.label.configure(image = self.image_widget)
        del drawnImage

    def save_image_info(self, imageIdx, x1,y1,x2,y2,age,gender):
        print self.images_info
        print self.images[imageIdx]
        self.images_info[self.images[imageIdx]].append((x1,y1,x2,y2,0,0))
        print self.images_info

    def load_image_info(self, imageIdx):
        pass

    def prev_click(self, event):
        self.curImageIdx -= 1
        if self.curImageIdx < 0:
            self.curImageIdx += len(self.images)
        self.show_image(self.curImageIdx)

    def next_click(self, event):
        self.curImageIdx += 1
        if self.curImageIdx >= len(self.images):
            self.curImageIdx -= len(self.images)
        self.show_image(self.curImageIdx)

    def clean_label_info(self, event):
        pass
    
def main():
    obj = APP()
    mainloop()

if __name__ == '__main__':
    main()
