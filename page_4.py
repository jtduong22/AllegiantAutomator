from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

def parse_hotel_page(driver, wait, is_hotel_booked):
    hotel_price = '0.00'

    if is_hotel_booked:
        print("Waiting for page to load. . .")
        wait.until(ec.presence_of_element_located((By.ID, "hotelchooser")))

        print("Page loaded. Retrieving price of first hotel")
        hotel_chooser = driver.find_element_by_id("hotelchooser")
        hotel_listing = hotel_chooser.find_element_by_xpath('.//div[4]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]')

        print("Price found. Selecting hotel")
        hotel_price = hotel_listing.find_element_by_xpath('.//strong').text
        hotel_listing.find_element_by_tag_name("button").click()

        print("Looking for book button")
        book_button = hotel_chooser.find_element_by_xpath('.//div[4]/div[2]/div[1]/div/div[3]/div/div[1]/div/div/ul/li[1]/div[1]/div[2]/div/div[2]/div/div[2]/button')
        book_button.click()


    print(f"added hotel price is {hotel_price}")

    print("Moving onto the next page\n")

    # Wait until button is enabled
    if not is_hotel_booked:
        # wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, "white-overlay")))
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='hotelchooser']/div[5]/div/button")))
        driver.find_element_by_xpath("//*[@id='hotelchooser']/div[5]/div/button").click()

    return [hotel_price]