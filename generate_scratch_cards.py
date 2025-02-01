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
    img = Image.new('RGB', (150, 150), color=random.choice(colors))  # Size adjusted to 150x150
    d = ImageDraw.Draw(img)
    
    # Load a font
    font = ImageFont.truetype('arial.ttf', 50)  # You can change the font as desired
    
    # Draw the number with black font (black text)
    d.text((50, 50), str(number), font=font, fill=(0, 0, 0))  # Black text

    # Apply rounded corners
    rounded_img = Image.new('RGBA', (150, 150), (0, 0, 0, 0))  # Use RGBA for transparency
    rounded_draw = ImageDraw.Draw(rounded_img)
    rounded_draw.rounded_rectangle([0, 0, 150, 150], radius=20, fill=random.choice(colors))

    # Create a mask using the alpha channel for transparency
    mask = rounded_img.convert("L")  # Convert to grayscale
    img.paste(rounded_img, (0, 0), mask)  # Apply the mask with transparency to the image
    
    # Save the generated image
    img.save(f'scratch_card_{i}.png')
