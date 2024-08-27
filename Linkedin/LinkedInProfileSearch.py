from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Selenium options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Avoid sandbox issues
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome resource limits

# Initialize WebDriver with WebDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to LinkedIn login page
    driver.get('https://www.linkedin.com/login')

    # Input your credentials
    username_field = driver.find_element(By.ID, 'username')
    password_field = driver.find_element(By.ID, 'password')
    username_field.send_keys('Replace with your email')  # Replace with your email
    password_field.send_keys('Replace with your email')            # Replace with your password

    # Click the login button
    login_button = driver.find_element(By.CSS_SELECTOR, 'button.btn__primary--large')
    login_button.click()

    # Wait for the LinkedIn home page to load
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-global-typeahead__input')))

    # Example of searching for a profile
    search_box = driver.find_element(By.CSS_SELECTOR, 'input.search-global-typeahead__input')
    search_box.send_keys('John Doe')  # Replace with the name you are searching for
    search_box.send_keys(Keys.RETURN)  # Simulate pressing Enter

    # Wait for search results to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.search-result__result-link')))

    # Click on the first profile in the search results
    first_profile = driver.find_element(By.CSS_SELECTOR, 'a.search-result__result-link')
    first_profile.click()

    # Wait for the profile page to load
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2.pv-entity__secondary-title')))

    # Extract role information
    try:
        role_element = driver.find_element(By.CSS_SELECTOR, 'h2.pv-entity__secondary-title')
        role = role_element.text
        print(f'Role: {role}')
    except Exception as e:
        print(f'Role not found: {e}')

finally:
    # Close the browser
    driver.quit()
