from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Edge browser (no path needed if driver is in same folder)
driver = webdriver.Edge()

# Open Google
driver.get("https://www.google.com")

# Find search box
search_box = driver.find_element(By.NAME, "q")

# Print result
print("Found:", search_box)

# Close browser
driver.quit()









from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

service = Service("C:\\Users\\muthi\\OneDrive\\JAVA PROGRAMING\\Documents\\Desktop\\msedgedriver.exe")

driver = webdriver.Edge(service=service)

# Open Facebook
driver.get("https://www.facebook.com/")
time.sleep(3)

# Find elements
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")
login = driver.find_element(By.NAME, "login")

# Enter details
email.send_keys("your_email")
password.send_keys("your_password")

# Click login
login.click()
time.sleep(5)

# Check login
if "facebook.com" in driver.current_url:
    print("Login successful!")
else:
    print("Login failed!")

input("Press Enter to close...")
driver.quit()






from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open Edge
driver = webdriver.Edge()

driver.get("https://www.google.com")
driver.maximize_window()

# Search Box
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Web Testing")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Search Button (optional)
search_button = driver.find_element(By.NAME, "btnK")
print("Google Search button found")

# Apps Button (may change sometimes)
try:
    apps_button = driver.find_element(By.CLASS_NAME, "gb_D")
    print("Google Apps button found")
except:
    print("Apps button not found")

# Sign-in Button
sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
print("Sign-in button found")

# Footer links
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.text, "->", link.get_attribute("href"))

# Hold browser
input("Press Enter to close...")

driver.quit()
