import os
from PIL import Image

class ConvertImage:
    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.format = path.split('.')[-1].lower()
        self.image = Image.open(self.path);
        self.rgb_image = self.image.convert('RGB');
    
    def ToPng(self):
        return self.rgb_image.save(f"{self.path.split('.')[0]}.png")
        
    def ToJpg(self):
        if self.format == 'jpeg':
            os.rename(self.path, os.path.join(os.path.dirname(self.path), self.name + ".jpg"))
            return 
        return self.rgb_image.save(f"{os.path.basename(self.path).split('.')[0]}.jpg")
    
    def ToJpeg(self):
        if self.format == 'jpg':
            os.rename(self.path, os.path.join(os.path.dirname(self.path), self.name + ".jpg"))
            return 
        return self.rgb_image.save(f"{os.path.basename(self.path).split('.')[0]}.jpeg")

    def ToTiff(self):
        return self.rgb_image.save(f"{os.path.basename(self.path).split('.')[0]}.tiff")

    def ToPDF(self):
        return self.rgb_image.save(f"{os.path.basename(self.path).split('.')[0]}.pdf")

    def ToEps(self):
        return self.rgb_image.save(f"{os.path.basename(self.path).split('.')[0]}.eps")

    def ToGif(self):
        return self.rgb_image.save(f"{os.path.basename(self.path).split('.')[0]}.gif")



if __name__ == "__main__":
    ConvertImage("test\img\pic.jpg").ToPDF()
    ConvertImage("test\img\pic.jpg").ToPng()
    #ConvertImage("test\img\pic.png").ToJpg()
    ConvertImage("test\img\pic.jpg").ToTiff()
    ConvertImage("test\img\pic.tiff").ToSvg()

