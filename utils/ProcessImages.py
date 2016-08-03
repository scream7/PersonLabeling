import glob
from PIL import Image

class ProcessImages():
    def __init__(self, path):
        if path[-1] != '/':
            path += '/'
        self.imagelist = glob.glob(path+'*.jpg')
    def GetImageList(self):
        return self.imagelist
        
if __name__ == '__main__':
    obj = ProcessImages('../images')
    print obj.GetImageList()
