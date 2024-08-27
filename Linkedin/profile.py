from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Load your list
data = pd.read_csv('your_list.csv')

# Set up Selenium options
chrome_options = Options()
# Optionally, enable headless mode for background execution
# chrome_options.add_argument("--headless")

# Initialize WebDriver with WebDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    print("Navigating to LinkedIn login page...")
    driver.get('https://www.linkedin.com/login')

    print("Logging in...")
    # Log in to LinkedIn
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    username = driver.find_element(By.ID, 'username')
    username.send_keys('Replace with your email')  # Replace with your email

    password = driver.find_element(By.ID, 'password')
    password.send_keys('Replace with your password')  # Replace with your password
    password.send_keys(Keys.RETURN)

    # Wait for login to complete
    print("Waiting for login to complete...")
    # try:
    #     # Wait for a common element that confirms successful login
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/feed/"]'))  # Example selector for the LinkedIn feed link
    #     )
    #     print("Login successful.")
    # except TimeoutException:
    #     print("Login failed or took too long. Check for errors or unexpected redirects.")
    #     driver.quit()
    #     exit()

    # Loop through the list
    profiles = []

    for index, row in data.iterrows():
        name = row['Name']
        org = row['Organization']

        print(f"\nSearching for {name} at {org}...")

        # Perform LinkedIn search
        search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
        search_bar.clear()
        search_bar.send_keys(f"{name} {org}")
        search_bar.send_keys(Keys.RETURN)

        # Wait for results to load
        print("Waiting for search results to load...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search-nec__hero-kcard-v2'))
        )

        # Extract profile details
        search_results = driver.find_elements(By.CLASS_NAME, 'search-nec__hero-kcard-v2')
        for result in search_results:
            try:
               # profile_link = result.find_element(By.CSS_SELECTOR, 'a.app-aware-link').get_attribute('href')
                profile_name = result.find_element(By.CSS_SELECTOR, 'div.search-nec__hero-kcard-v2-content .search-nec__hero-kcard-v2-title').text
                profile_title = result.find_element(By.CLASS_NAME, 'entity-result__primary-subtitle').text
                profiles.append(( name,profile_title))
                print(f"Found profile: {profile_name},  Title: {profile_title}")
            except Exception as e:
                print(f"Error extracting profile details: {e}")

        time.sleep(2)  # Adjust or remove as needed

    # Add the profiles to your data and save
    print("\nAdding profiles to the data and saving...")
    profiles_df = pd.DataFrame(profiles, columns=['Profile Name',  'Profile Title'])
    profiles_df.to_csv('profiles_list.csv', index=False)
    print("Data saved to 'profiles_list.csv'.")

finally:
    print("\nClosing the browser...")
    driver.quit()
    print("Browser closed.")
