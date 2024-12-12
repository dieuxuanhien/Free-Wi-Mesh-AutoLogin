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
edge_driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "msedgedriver.exe"))
if not os.path.exists(edge_driver_path):
    raise FileNotFoundError(f"Edge WebDriver not found at {edge_driver_path}")


# Set up the WebDriver
edge_options = edgeOptions()
edge_options.add_argument("--headless=new")
edge_options.add_argument("--start-maximized")
edge_driver_service = Service(edge_driver_path)
print(f"Using Edge WebDriver at: {edge_driver_path}")


def check_internet_connection():
    """Check if the internet connection is active."""
    try:
        urllib.request.urlopen("https://www.google.com", timeout=5)
        return True
    except urllib.error.URLError:
        return False
    except Exception as e:
        print(f"Unexpected error while checking internet connection: {e}")
        return False


def execute_connect():
    driver = None
    try:
        driver = webdriver.Edge(service=edge_driver_service, options=edge_options)
        driver.get("http://192.168.1.1")  # Replace with the actual login URL
        time.sleep(10)
        # Wait for the page to load and click the first button
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'logo_button'))  # Update ID if needed
        ).click()

        # Scroll to the bottom of the page and wait for the second button
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "connectToInternet"))  # Update ID if needed
        ).click()

        print("Logged in or refreshed successfully.")
    except Exception as e:
        print(f"Error during connection: {e}")
    finally:
        if driver:
            driver.quit()
    



while (True):
    if(check_internet_connection() == False): 
        try:
            execute_connect()
        except:
            print("FAILED")
        finally:
            time.sleep(3)

    else:
        print("ALREADY CONNECTED, SLEEPING")
        time.sleep(2)
        