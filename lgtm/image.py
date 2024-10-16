import os

from PIL import Image
def thumbnail(infile, size=(128, 128)):
    outfile = os.path.splitext(   #split으로 파일명으로 만들고 thumbnail로 확장자붙임
        infile)[0] + ".thumbnail"
    try:
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(outfile, "JPEG")
    except IOError:
        print("cannot create thumbnail for", infile)

if __name__=="__main__":
    thumbnail(r"C:\workspace\Imenv\Imenv\lgtm\tests\data\test_image.jpg")

