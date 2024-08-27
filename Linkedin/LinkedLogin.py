from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Selenium options
chrome_options = Options()
# Optionally, remove the headless mode for testing
# chrome_options.add_argument("--headless")

# Initialize WebDriver with WebDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open LinkedIn login page
    driver.get('https://www.linkedin.com/login')
    
    # Wait for the username field to be present and enter the username
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys('Replace with your email')  # Replace with your email

    # Enter the password
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('Replace with your email')  # Replace with your password

    # username_field.send_keys('bhupentiwari@live.com')  # Replace with your email
    # password_field.send_keys('Docker#501')            # Replace with your password
    # Submit the login form
    password_field.submit()

    # Wait for a successful login indication
    try:
        # Change the selector to an element that indicates a successful login
        success_indicator = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-control-name="nav_home"]'))  # Example selector
        )
        print("Login successful!")
    except Exception as e:
        print("Login failed or took too long:", e)

finally:
    # Close the browser after a delay to see the result
    time.sleep(5)
    driver.quit()
