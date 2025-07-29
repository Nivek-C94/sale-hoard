from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def launch_ebay_lister(metadata: dict, images: list, credentials: dict):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.ebay.com/signin/")
    
    # Login sequence
    driver.find_element(By.ID, "userid").send_keys(credentials['username'])
    driver.find_element(By.ID, "signin-continue-btn").click()
    time.sleep(2)
    driver.find_element(By.ID, "pass").send_keys(credentials['password'])
    driver.find_element(By.ID, "sgnBt").click()

    time.sleep(3)
    driver.get("https://www.ebay.com/sl/sell")  # New listing page
    time.sleep(3)

    # Title
    driver.find_element(By.ID, "title").send_keys(metadata['title'])

    # Description
    desc_box = driver.find_element(By.ID, "item-description-textbox")
    desc_box.send_keys(metadata['description'])

    # Category Auto or placeholder
    # Skip category assignment – handled by eBay or add custom logic

    # Price
    price_input = driver.find_element(By.NAME, "price")
    price_input.clear()
    price_input.send_keys(str(metadata['price']))

    # Image Upload (manual or desktop auto-insert)
    for image_path in images:
        upload_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        upload_input.send_keys(image_path)
        time.sleep(1.5)

    # Submit
    driver.find_element(By.ID, "action_preview").click()  # Could be 'action_publish'
    
    time.sleep(5)
    listing_url = driver.current_url
    driver.quit()
    return listing_url


# Example usage:
if __name__ == '__main__':
    dummy_metadata = {
        'title': 'Sony WH-1000XM4 Wireless Noise Cancelling Headphones - Black',
        'description': 'Gently used, includes original case and charger. Fully functional.',
        'price': 220
    }
    dummy_images = ["/path/to/Sony1.jpg", "/path/to/Sony2.jpg"]
    dummy_creds = {'username': 'your-email@example.com', 'password': 'your-password'}
    url = launch_ebay_lister(dummy_metadata, dummy_images, dummy_creds)
    print("Listing created at:", url)