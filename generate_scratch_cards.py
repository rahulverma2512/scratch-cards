from PIL import Image, ImageDraw, ImageFont
import random

# Define a list of colors for the background
colors = [
    (255, 99, 71),  # Tomato
    (0, 128, 0),    # Green
    (135, 206, 235),# Sky Blue
    (0, 128, 128),  # Teal Blue
    (255, 215, 0),  # Gold
    (0, 100, 0),    # Dark Green
    (47, 79, 79),   # Dark Slate Gray
]

# Create a list with each number (1 to 12) appearing exactly 3 times
numbers = [i for i in range(1, 13)] * 3

# Shuffle the numbers list to randomize the order
random.shuffle(numbers)

# Create scratch cards for 36 participants
for i in range(1, 37):  # Adjust the range for the number of participants
    number = numbers[i - 1]  # Get the number from the shuffled list
    img = Image.new('RGB', (150, 150), color=random.choice(colors))  # Size adjusted to 150x150
    d = ImageDraw.Draw(img)
    
    # Load a bold font with size 80 (ensure you have Arial-Bold.ttf or use another bold font)
    try:
        font = ImageFont.truetype('arialbd.ttf', 80)  # 'arialbd.ttf' is the bold version of Arial
    except IOError:
        font = ImageFont.truetype('arial.ttf', 80)  # Fallback to regular Arial if bold is not available
    
    # Get the bounding box for the text
    bbox = d.textbbox((0, 0), str(number), font=font)
    text_width = bbox[2] - bbox[0]  # Width of the text
    text_height = bbox[3] - bbox[1]  # Height of the text
    
    # Calculate the x position to center the text
    x_position = (150 - text_width) / 2
    
    # Draw the number with black bold font (black text)
    d.text((x_position, 30), str(number), font=font, fill=(0, 0, 0))  # Black text
    
    # Apply rounded corners
    rounded_img = Image.new('RGBA', (150, 150), (0, 0, 0, 0))  # Use RGBA for transparency
    rounded_draw = ImageDraw.Draw(rounded_img)
    rounded_draw.rounded_rectangle([0, 0, 150, 150], radius=20, fill=random.choice(colors))

    # Create a mask using the alpha channel for transparency
    mask = rounded_img.convert("L")  # Convert to grayscale
    img.paste(rounded_img, (0, 0), mask)  # Apply the mask with transparency to the image
    
    # Save the generated image
    img.save(f'scratch_card_{i}.png')
