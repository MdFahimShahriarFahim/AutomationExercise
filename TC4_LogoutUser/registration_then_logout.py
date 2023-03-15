from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import ActionChains
import time

valid_username = "fahim"
valid_email = "fahim1@gmail.com"


def register_then_logout_user_valid(user_name, user_email):
    options1 = Options()
    options1.add_argument("--disable-notifications")
    driver_path = root_path(ignore_cwd=True) + "\Drivers\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options1)
    driver.maximize_window()
    driver.get("https://automationexercise.com/")

    home_page = driver.find_element(By.XPATH, "/html/body").is_displayed()
    print(f"Verify that home page is visible successfully: {home_page}")

    # Signup / Login
    signup_btn = driver.find_element(By.LINK_TEXT, "Signup / Login")
    signup_btn.click()

    # New User Signup!
    signup_form = driver.find_element(By.XPATH, "/html//section[@id='form']//div[@class='col-sm-4']").is_displayed()
    print(f"Verify 'New User Signup!' is visible: {signup_form}")

    name_field = driver.find_element(By.NAME, "name")
    name_field.send_keys(user_name)

    email_field = driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > input[name='email']")
    email_field.send_keys(user_email)

    driver.find_element(By.CSS_SELECTOR, "[action='\/signup'] .btn-default").click()

    # ENTER ACCOUNT INFORMATION
    account_info_form = driver.find_element(By.XPATH, "/html//section[@id='form']//div[@class='col-sm-4 "
                                                      "col-sm-offset-1']").is_displayed()
    print(f"Verify that 'ENTER ACCOUNT INFORMATION' is visible: {account_info_form}")

    title = driver.find_element(By.ID, "id_gender1")
    title.click()

    password = driver.find_element(By.ID, "password")
    password.send_keys("12345")

    # Date of Birth
    Select(driver.find_element(By.XPATH, "/html//select[@id='days']")).select_by_visible_text("10")
    Select(driver.find_element(By.ID, "months")).select_by_visible_text("January")
    Select(driver.find_element(By.ID, "years")).select_by_visible_text("2021")

    # Checkbox1: Sign up for our newsletter! and Checkbox2: Receive special offers from our partners!
    driver.find_element(By.ID, "newsletter").click()
    driver.find_element(By.ID, "optin").click()

    # ADDRESS INFORMATION
    driver.find_element(By.ID, "first_name").send_keys("Test")
    driver.find_element(By.ID, "last_name").send_keys("Person")
    driver.find_element(By.ID, "company").send_keys("Avengers")
    driver.find_element(By.ID, "address1").send_keys("NY")
    driver.find_element(By.ID, "address2").send_keys("R-3")
    Select(driver.find_element(By.ID, "country")).select_by_visible_text("United States")
    driver.find_element(By.ID, "state").send_keys("State NY")
    driver.find_element(By.ID, "city").send_keys("City NY")
    driver.find_element(By.ID, "zipcode").send_keys("3030")
    driver.find_element(By.ID, "mobile_number").send_keys("01928373625")

    # Create Account Button
    driver.find_element(By.CSS_SELECTOR, ".col-sm-4.col-sm-offset-1  form[method='post'] > .btn.btn-default").click()

    # ACCOUNT CREATED!
    time.sleep(5)
    account_created = driver.find_element(By.XPATH, "//section[@id='form']//div[@class='row']").is_displayed()
    print(f"Verify that 'ACCOUNT CREATED!' is visible: {account_created}")
    driver.find_element(By.LINK_TEXT, "Continue").click()
    print("New User Registration successful!")

    # Logout User
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(4) > a").click()
    print("Logout Successful!")

    time.sleep(5)
    # driver.close()


register_then_logout_user_valid(valid_username, valid_email)
