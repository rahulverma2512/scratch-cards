from PIL import Image, ImageDraw, ImageFont
import random

# Define a list of colors for the background
colors = [
    (255, 99, 71),  # Tomato
    (255, 165, 0),  # Orange
    (0, 128, 0),    # Green
    (135, 206, 235),# Sky Blue
    (255, 69, 0),   # Red-Orange
    (123, 104, 238),# Medium Slate Blue
    (255, 215, 0),  # Gold
    (255, 182, 193),# Light Pink
    (255, 255, 0),  # Yellow
    (238, 130, 238),# Violet
]

# Create scratch cards for 36 participants
for i in range(1, 37):  # Adjust the range for the number of participants
    number = random.randint(1, 12)  # Random number for team assignment
    img = Image.new('RGB', (300, 150), color=random.choice(colors))  # Choose a random background color
    d = ImageDraw.Draw(img)
    
    # Load a font
    font = ImageFont.truetype('arial.ttf', 50)  # You can change the font as desired
    
    # Draw the number with black font
    d.text((100, 50), str(number), font=font, fill=(0, 0, 0))  # Black text

    # Save the generated image
    img.save(f'scratch_card_{i}.png')
