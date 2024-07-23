from PIL import Image, ImageColor, ImageFilter, ImageFont, ImageDraw, ImageOps

img = Image.open('C:\\Users\\User\\Pictures\\пейзаж.jpg')

r, g, b = img.split()
img = Image.merge(mode='RGB', bands=(b, g, r))
new_img = img.resize((1200, 800))
new_img.save('C:\\Users\\User\\Pictures\\новый_пейзаж.jpg')

# Метод, позволяющий создавать изображения с нуля

total_new = Image.new('RGB', (800, 800), ImageColor.getrgb('#2fa1ac'))
total_new.paste(new_img, (0, 400))
total_new = total_new.filter(ImageFilter.GaussianBlur(radius=1))

total_new = ImageOps.mirror(total_new)
total_new = ImageOps.posterize(total_new, 3)
draw = ImageDraw.Draw(total_new)
text = 'Welcome to Wild'
font = ImageFont.truetype("arial.ttf", 20)
draw.text((400, 400), text=text, font=font, fill='black')
total_new.show()
