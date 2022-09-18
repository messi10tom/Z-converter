from PIL import Image

class Image2Image:
    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.format = path.split('.')[-1].lower()
        self.image = Image.open(self.path);
        self.rgb_image = self.image.convert('RGB');
    
    def ToPng(self):
        return self.rgb_image.save(f"{self.path.split('.')[0]}.png")
    
#     def jpg2jpeg(self):
#         os.rename(self.path, os.path.join(os.path.dirname(self.path), self.name + ".jpeg"))
# 
#     def jpeg2jpg(self):
#         os.rename(self.path, os.path.join(os.path.dirname(self.path), self.name + ".jpg"))
        
    def ToJpg(self):
        return self.rgb_image.save(f"{self.path.split('.')[0]}.jpg")

    def ToTiff(self):
        return self.rgb_image.save(f"{self.path.split('.')[0]}.tiff")

    def ToPDF(self):
        return self.rgb_image.save(f"{self.path.split('.')[0]}.pdf")

    def ToEps(self):
        return self.rgb_image.save(f"{self.path.split('.')[0]}.eps")

    def ToGif(self):
        return self.rgb_image.save(f"{self.path.split('.')[0]}.gif")



if __name__ == "__main__":
    Image2Image("test\img\pic.jpg").ToPDF()
    Image2Image("test\img\pic.jpg").ToPng()
    #Image2Image("test\img\pic.png").ToJpg()
    Image2Image("test\img\pic.jpg").ToTiff()
    Image2Image("test\img\pic.tiff").ToSvg()

