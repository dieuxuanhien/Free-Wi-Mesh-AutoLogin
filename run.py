from selenium import webdriver
from selenium.webdriver.edge.options import Options as edgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import time
import urllib.request
import os


# start edge driver
edge_driver_path = os.path.dirname(__file__)
edge_driver_path += "\msedgedriver.exe"
edge_driver_service = Service(edge_driver_path)
print(edge_driver_path)

# Set up the WebDriver
edge_options = edgeOptions()
edge_options.add_argument("--headless=new")
edge_options.add_argument("--start-maximized")


def check_internet_connection():
    try:
        urllib.request.urlopen("https://www.google.com")
        return True
    except urllib.error.URLError:
        return False


def execute_connect():
    driver= webdriver.Edge(service = edge_driver_service,options = edge_options)
  
    driver.get("http:/192.168.1.1")  # Replace with the actual login URL

    # Wait for the page to load (you may need to adjust this)
    time.sleep(3)
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'logo_button'))  # Use the correct ID or selector
        ).click()  # Click the login button

        
    # Wait for the second button to be clickable
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "connectToInternet"))  # Use the correct ID or selector
        ).click()  # Click the login button
    print("Logged in or refreshed.")
    time.sleep(10)
    driver.quit()
    



while (True):
    if(check_internet_connection() == False): 
        try:
            execute_connect()
        except:
            print("FAILED")

    else:
        print("ALREADY CONNECTED, SLEEPING")
        time.sleep(2)
        