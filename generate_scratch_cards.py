from PIL import Image, ImageDraw, ImageFont
import random

for i in range(1, 37):  # Adjust the range for the number of participants
    number = random.randint(1, 12)
    img = Image.new('RGB', (300, 150), color='gray')
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', 50)
    d.text((100, 50), str(number), font=font, fill=(255, 255, 255))
    img.save(f'scratch_card_{i}.png')
