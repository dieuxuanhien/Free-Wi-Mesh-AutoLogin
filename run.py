from selenium import webdriver
from selenium.webdriver.edge.options import Options as edgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
import os


# start edge driver
path = os.path.dirname(__file__)
path+= "\msedgedriver.exe"

print(path)

while( True):
    try :
        os.startfile(path)
        break
    except:
        print("Failed")


# Set up the WebDriver
edge_options = edgeOptions()
edge_options.add_argument("--headless=new")
edge_options.add_argument("--start-maximized")
driver = webdriver.Edge(options = edge_options)



def check_internet_connection():
    try:
        urllib.request.urlopen("https://www.google.com")
        return True
    except urllib.error.URLError:
        return False


def execute_connect():
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
    driver.quit



while (True):
    if(check_internet_connection() == False): 
        try:
            execute_connect()
        except:
            print("FAILED")

    else:
        print("ALREADY CONNECTED, SLEEPING")
        time.sleep(5)
        