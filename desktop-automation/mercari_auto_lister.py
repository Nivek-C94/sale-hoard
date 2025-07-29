from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def launch_mercari_lister(metadata: dict, images: list, credentials: dict):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.mercari.com/us/login")
    time.sleep(2)

    # Login
    driver.find_element(By.NAME, "email").send_keys(credentials['username'])
    driver.find_element(By.NAME, "password").send_keys(credentials['password'])
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(5)

    # Navigate to sell page
    driver.get("https://www.mercari.com/sell/")
    time.sleep(3)

    # Title
    driver.find_element(By.NAME, "name").send_keys(metadata['title'])

    # Description
    driver.find_element(By.NAME, "description").send_keys(metadata['description'])

    # Price
    price_input = driver.find_element(By.NAME, "price")
    price_input.clear()
    price_input.send_keys(str(metadata['price']))

    # Image Upload
    for image_path in images:
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        file_input.send_keys(image_path)
        time.sleep(1.5)

    # Submit
    driver.find_element(By.XPATH, "//button[contains(text(), 'List')]" ).click()
    time.sleep(5)
    listing_url = driver.current_url
    driver.quit()
    return listing_url


if __name__ == '__main__':
    dummy_metadata = {
        'title': 'Logitech MX Master 3 Wireless Mouse',
        'description': 'Works flawlessly. Slight cosmetic wear. Includes USB dongle.',
        'price': 55
    }
    dummy_images = ["/path/to/mouse1.jpg"]
    dummy_creds = {'username': 'your-email@example.com', 'password': 'your-password'}
    url = launch_mercari_lister(dummy_metadata, dummy_images, dummy_creds)
    print("Mercari Listing URL:", url)