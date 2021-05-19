print('''
 Catware Pixel-Art Block Generator
''')

pixels_ = [" ", "▒", "█"]
buffer = ""
debug = False
times = 2
br = []

mediums = [
100,
101,
102,
103,
104,
105,
106,
107,
108,
109,
110,
111,
112,
113,
114,
115,
116,
117,
118,
119,
120,
121,
122,
123,
124,
125,
126,
127,
128,
129,
130
]

path = input(" >>> Укажите путь к изображению: ")
from PIL import Image
im = Image.open(path)
img = im
print(" >>> Изображение открыто.")
pixels = im.load() # create the pixel map
print(" >>> Изображение загружено. Обработка изображения...")
width, height = im.size
print(f"Получен размер изображения: {width}x{height}")
for i in range(height): # for every pixel:
    for j in range(width):
        for x in range(times):
            try:
                pixel = pixels[j,i]
                brightness = sum(pixel)/3 ##0 = пробел и 255 - full block (белый) 
                if brightness < 128:
                    buffer += pixels_[0]
                elif int(brightness) in mediums:
                    buffer += pixels_[1]
                elif brightness > 128:
                    buffer += pixels_[2]
                if debug:
                    if str(int(brightness)) not in br:
                        br += str(int(brightness))
            except:
                buffer += "?"
    buffer += '\n'
print(buffer)
if debug:
    print("Яркости: " + ", ".join(br))
