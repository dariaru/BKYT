from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from PIL import Image, ImageDraw

def fiduresDraw(radius, side, height):
    image = Image.new("RGBA", (750, 750), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((150, 150, radius * 150, radius * 150), fill='green', outline='green')
    draw.rectangle((0, 0, side * 100, side * 100), fill='red', outline='black')
    draw.rectangle((0, 0, side * 100, height * 100), fill='darkblue', outline='darkblue')
    image.show()

def main():
    side = 3
    height = 2
    radius = 5
    r = Rectangle("синего", side, height)
    c = Circle("зеленого", radius)
    s = Square("красного", side)
    print(r)
    print(c)
    print(s)
    fiduresDraw(radius, side, height)


if __name__ == "__main__":
    main()
