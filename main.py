from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from test.test_pickle import getattribute

# OpenSooq Cars URL
uri = 'https://ly.opensooq.com/ar/%d8%b3%d9%8a%d8%a7%d8%b1%d8%a7%d8%aa-%d9%88-%d9%85%d8%b1%d9%83%d8%a8%d8%a7%d8%aa/%d8%b3%d9%8a%d8%a7%d8%b1%d8%a7%d8%aa-%d9%84%d9%84%d8%a8%d9%8a%d8%b9'

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get(uri)
time.sleep(3)  # Allow page to load

def main():
    print('Getting cars...')

    page = 1
    cars_data = []  # Store car details in a list

    while page < 30:  # Loop through first 7 pages
        try:
            # Click next page button
            next_page = driver.find_element(By.XPATH, f"//*[@data-id='page_{page}']")
            next_page.click()
            time.sleep(3)  # Allow time for page to load
            page += 1

            # Extract 30 car listings per page
            for i in range(30):
                try:
                    card_car = driver.find_element(By.XPATH, f"//*[@data-id='post_{i}']")
                    name = card_car.find_element(By.TAG_NAME, 'h2').text
                    price = card_car.find_element(By.CLASS_NAME, "priceColor").text
                    img = card_car.find_element(By.TAG_NAME, 'img').get_attribute('src')
                    link = card_car.get_attribute('href')

                    print(f"Name: {name}, Price: {price} , Image: {img}, Link: {link}")
                    # Append data to the list
                    cars_data.append([name, price, img,link])
                except Exception as e:
                    print(e)   # Skip if element is not found
                    continue  # Skip if element is not found

        except Exception as e:
           print(e)
           break  # Stop if no more pages exist

    # Convert list to DataFrame
    df = pd.DataFrame(cars_data, columns=["Name", "Price", "Image", "Link"])

    # Save to Excel
    df.to_excel("cars.xlsx", index=False)
    print("Data saved to cars.xlsx")

    driver.quit()  # Close the browser

if __name__ == '__main__':
    main()
