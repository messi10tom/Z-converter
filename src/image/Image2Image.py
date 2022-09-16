from PIL import Image

class Image2Image:
    def __init__(self, path):
        self.path = path
        self.extension = path.split('.')[-1]
    
    def ToPng(self):
        image = Image.open(self.path);
        rgb_image = image.convert('RGB');
        rgb_image.save(f"{self.path.split('.')[0]}.png") # save image as png

if __name__ == "__main__":
    Image2Image("test\pic.jpg").ToPng()

