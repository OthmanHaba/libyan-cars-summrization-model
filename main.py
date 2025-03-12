from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from test.test_pickle import getattribute

# OpenSooq Cars URL
uri = 'https://ly.opensooq.com/en/%d8%b3%d9%8a%d8%a7%d8%b1%d8%a7%d8%aa-%d9%88-%d9%85%d8%b1%d9%83%d8%a8%d8%a7%d8%aa/%d8%b3%d9%8a%d8%a7%d8%b1%d8%a7%d8%aa-%d9%84%d9%84%d8%a8%d9%8a%d8%b9'

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get(uri)
time.sleep(3)  # Allow page to load

def main():
    print('Getting cars...')

    page = 0
    cars_data = []  # Store car details in a list

    page_counter = 0
    while page_counter < 40:  # Loop through first 7 pages
        try:
            # Click next page button
            next_page = driver.find_element(By.XPATH, f"//*[@data-id='page_{page}']")
            next_page.click()
            time.sleep(3)  # Allow time for page to load
            if(page == 9):
                page = 0
            page += 1
            page_counter += 1

            # Extract 30 car listings per page
            for i in range(30):
                try:
                    card_car = driver.find_element(By.XPATH, f"//*[@data-id='post_{i}']")
                    # name = card_car.find_element(By.TAG_NAME, 'h2').text
                    details = card_car.find_element(By.TAG_NAME,'p').text

                    price = card_car.find_element(By.CLASS_NAME, "priceColor").text
                    img = card_car.find_element(By.TAG_NAME, 'img').get_attribute('src')
                    link = card_car.get_attribute('href')
                    detArray = details.split(',')
                    co = detArray[1]
                    model= detArray[2]
                    year= detArray[4]
                    miles = detArray[5] + detArray[6] + detArray[7]

                    print(f"Price: {price} , Image: {img}, Link: {link} , Country: {co} , Model: {model} , Year: {year} , Miles: {miles}")
                    # Append data to the list
                    cars_data.append([co,model,year,miles,price, img,link])

                except Exception as e:
                    print(e)   # Skip if element is not found
                    continue  # Skip if element is not found

        except Exception as e:
           print(e)
           break  # Stop if no more pages exist

    # Convert list to DataFrame
    df = pd.DataFrame(cars_data, columns=["Co", "Model", "Year" ,"Miles", "Price", "Image", "Link"])

    # Save to Excel
    df.to_excel("cars.xlsx", index=False)
    print("Data saved to cars.xlsx")

    driver.quit()  # Close the browser

if __name__ == '__main__':
    main()
