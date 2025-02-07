from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import urllib.parse
import time

# ChromeDriver setup
chrome_driver_path = 'C:/Users/lenovo/Downloads/chromedriver-win64/chromedriver.exe'
service = Service(chrome_driver_path)
options = Options()
options.add_argument('--disable-notifications')
options.add_argument('--disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--start-maximized')
driver = webdriver.Chrome(service=service, options=options)

# Load data from the Excel sheet
data = pd.read_excel('D:/My softwares and scripts/Scratch-card/scratch-cards/whatsapp_links.xlsx')

for index, row in data.iterrows():
    name = row['name']
    phone_number = str(row['phone_number'])
    hyperlink = row['hyperlink']
    
    # Beautified message template
    message_template = (
        f"Hi {name},\n\n"
        f"✨ Please click this link to scratch your card 👉 {hyperlink} 🎁\n\n"
        "Thanks,\nCharu"
    )
    
    # Encode the message for URL compatibility
    encoded_message = urllib.parse.quote(message_template)
    
    # Construct the WhatsApp URL
    whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
    
    # Open WhatsApp Web
    driver.get(whatsapp_url)
    
    # Wait for WhatsApp Web to fully load
    time.sleep(10)
    
    try:
        # Wait for the send button and click it
        send_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']"))
        )
        send_button.click()
        time.sleep(2)
    except Exception as e:
        print(f"Error sending message to {name}: {str(e)}")

driver.quit()
