from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time


def add_product_cart_valid():
    # 1. Launch browser
    options1 = Options()
    options1.add_argument("--disable-notifications")
    driver_path = root_path(ignore_cwd=True) + "\Drivers\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options1)
    driver.maximize_window()

    # 2. Navigate to url
    driver.get("https://automationexercise.com/")

    # 3. Verify that home page is visible successfully
    home_page = driver.find_element(By.XPATH, "/html/body").is_displayed()
    print(f"Verify that home page is visible successfully: {home_page}")

    # 4. Click 'Products' button
    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(2) > a").click()
    time.sleep(5)

    # 5. Hover over first product and click 'Add to cart'
    product_1 = driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > .product-image-wrapper > .single-products "
                                                     "> .productinfo.text-center")
    ActionChains(driver).move_to_element(product_1).perform()
    driver.find_element(By.CSS_SELECTOR, ".features_items [class='col-sm-4']:nth-child(3) div:nth-of-type(2) "
                                         ".add-to-cart").click()
    time.sleep(5)

    # 6. Click 'Continue Shopping' button
    driver.find_element(By.XPATH, "/html//div[@id='cartModal']//button[.='Continue Shopping']").click()
    time.sleep(5)

    # 7. Hover over second product and click 'Add to cart'
    product_2 = driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > .product-image-wrapper > .single-products "
                                                     "> .productinfo.text-center")
    ActionChains(driver).move_to_element(product_2).perform()
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > .product-image-wrapper > .single-products > "
                                         ".product-overlay > .overlay-content > .add-to-cart.btn.btn-default").click()
    time.sleep(5)

    # 8. Click 'View Cart' button
    driver.find_element(By.LINK_TEXT, "View Cart").click()
    time.sleep(5)

    # 9. Verify both products are added to Cart
    cart_verify = driver.find_element(By.CSS_SELECTOR, "table#cart_info_table > tbody").is_displayed()
    print(f"Verify both products are added to Cart: {cart_verify}")
    time.sleep(3)

    # 10. Verify their prices, quantity and total price
    price_verify = driver.find_element(By.CSS_SELECTOR, "tr:nth-of-type(1) > .cart_price").is_displayed()
    quantity_verify = driver.find_element(By.CSS_SELECTOR, "tr:nth-of-type(1) > .cart_quantity").is_displayed()
    total_price_verify = driver.find_element(By.CSS_SELECTOR, "tr:nth-of-type(1) > .cart_total").is_displayed()
    print(f"Verify their prices: {price_verify}, quantity: {quantity_verify} and total price: {total_price_verify}")
    time.sleep(3)


add_product_cart_valid()
