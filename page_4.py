from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

def parse_hotel_page(driver, wait):
    hotel_price = '0.00'

    print(f"added hotel price is ${hotel_price}")

    # Wait until button is enabled
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "continue")))
    print("Moving onto the next page\n")
    driver.find_element_by_class_name("continue").click()