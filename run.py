from selenium import webdriver
from selenium.webdriver.edge.options import Options as edgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import time
import urllib.request
import os

# Configure Edge WebDriver
edge_driver_path = os.path.abspath("msedgedriver.exe")
if not os.path.exists(edge_driver_path):
    raise FileNotFoundError(f"Edge WebDriver not found at {edge_driver_path}")

edge_options = edgeOptions()
edge_options.add_argument("--headless=new")
edge_options.add_argument("--start-maximized")
edge_driver_service = Service(edge_driver_path)

def check_internet_connection():
    """Check if the internet connection is active."""
    try:
        urllib.request.urlopen("https://www.google.com", timeout=5)
        return True
    except Exception:
        return False

def execute_connect():
    try:
        print("Launching WebDriver...")
        driver = webdriver.Edge(service=edge_driver_service, options=edge_options)
        driver.get("http://192.168.0.1")
        print("Page loaded. Waiting for elements...")
        for attemp in range(2):
            # Click the first button
            time.sleep(3)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "logo_button"))
            ).click()
            print("First button clicked.")

            # Scroll and click the second button
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(6)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "connectToInternet"))
            ).click()

            print("Second button clicked.")
        print("Connection initiated.")
    except Exception as e:
        print(f"Error: {e}")
        raise
    finally:
        if 'driver' in locals():
            driver.quit()

while True:
    if not check_internet_connection():
        print("No internet. Attempting to reconnect...")
        try:
            execute_connect()
        except Exception as e:
            print(f"Failed to reconnect: {e}")
        time.sleep(3)
    else:
        print("Internet is active. Sleeping...")
        time.sleep(10)
