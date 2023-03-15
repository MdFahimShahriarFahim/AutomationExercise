from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import ActionChains
import time

user_email_valid = "fahim1@gmail.com"


def login_then_logout_valid(user_email):
    # 1. Launch browser
    options1 = Options()
    options1.add_argument("--disable-notifications")
    driver_path = root_path(ignore_cwd=True) + "\Drivers\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options1)
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get("https://automationexercise.com/")

    # 3. Verify that home page is visible successfully
    home_page = driver.find_element(By.XPATH, "/html/body").is_displayed()
    print(f"Verify that home page is visible successfully: {home_page}")

    # 4. Click on 'Signup / Login' button
    signup_btn = driver.find_element(By.LINK_TEXT, "Signup / Login")
    signup_btn.click()

    # 5. Verify 'Login to your account' is visible
    login_form = driver.find_element(By.XPATH,
                                     "/html//section[@id='form']//div[@class='col-sm-4 col-sm-offset-1']").is_displayed()
    print(f"Verify Login to your account is visible: {login_form}")

    # 6. Enter correct email address and password
    driver.find_element(By.XPATH, "//section[@id='form']//div[@class='col-sm-4 col-sm-offset-1']//form["
                                  "@action='/login']/input[@name='email']").send_keys(user_email)
    driver.find_element(By.XPATH, "//section[@id='form']//div[@class='col-sm-4 col-sm-offset-1']//form["
                                  "@action='/login']/input[@name='password']").send_keys("12345")

    # 7. Click 'login' button
    driver.find_element(By.CSS_SELECTOR, ".login-form > form[method='post'] > .btn.btn-default").click()
    time.sleep(5)

    # 8. Verify that 'Logged in as username' is visible
    login_as_username = driver.find_element(By.XPATH, "/html//header[@id='header']/div[@class='header-middle']//ul["
                                                      "@class='nav navbar-nav']/li[10]/a").is_displayed()
    print(f"Verify that Logged in as username is visible: {login_as_username}")
    time.sleep(5)

    # 9. Click 'Logout' button
    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(4) > a").click()
    print("Logout Successful!")
    time.sleep(5)

    # 10. Verify that user is navigated to login page
    login_page_verify = driver.find_element(By.XPATH, "//section[@id='form']//div[@class='row']").is_displayed()
    print(f"Verify that user is navigated to login page: {login_page_verify}")
    time.sleep(3)


login_then_logout_valid(user_email_valid)
