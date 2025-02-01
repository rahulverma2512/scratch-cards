# File: generate_urls.py

# Define your GitHub Pages base URL for the dynamic HTML file
base_url = "https://rahulverma2512.github.io/scratch-cards/dynamic_scratch_card.html?cardUrl="

# Define the path to your scratch card images
image_base_url = "https://rahulverma2512.github.io/scratch-cards/scratch_card_"

# Read the list of participants
with open('participants.txt', 'r') as file:
    participants = file.readlines()

# Generate URLs for each participant
urls = []
for i, participant in enumerate(participants):
    card_url = f"{image_base_url}{i+1}.png"  # Adjust based on your image naming convention
    full_url = f"{base_url}{card_url}"
    urls.append(f"{participant.strip()}: {full_url}")

# Save the generated URLs to a file
with open('scratch_card_urls.txt', 'w') as file:
    file.write('\n'.join(urls))

print("URLs generated successfully and saved to scratch_card_urls.txt")
