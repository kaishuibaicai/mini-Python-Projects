from PIL import Image, ImageDraw

im = Image.open("a.jpg")
draw = ImageDraw.Draw(im)

line = 5
x, y = 10, 10
width, height = 100, 50
for i in range(1, line + 1):
    draw.rectangle((x + (line - i), y + (line - i), x + width + i, y + height + i), outline='red')

im.save("b.jpg")