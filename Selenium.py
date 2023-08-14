from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Edge('./msedgedriver.exe')

def open_page():
    driver.get("https://resale-aus.fwwc23.tickets.fifa.com/secured/selection/resale/item?performanceId=10228543141436&productId=101397765775&lang=en")
    time.sleep(2)
    #Find username
    username_found = False
    while username_found == False:
        try:
            username = driver.find_element(By.XPATH, '//*[@id="signInName"]')
            username_found = True
            print("Username field found!")
        except:
            time.sleep(3)
            print("Couldn't find username field! Pausing for 3 seconds.")
    #Send username
    username.send_keys("zackuo98@gmail.com")
    #Find password
    password_found = False
    while password_found == False:
        try:
            password = driver.find_element(By.XPATH, '//*[@id="password"]')
            password_found = True
            print("Password field found!")
        except:
            time.sleep(3)
            print("Couldn't find password field! Pausing for 3 seconds.")
    time.sleep(2)
    #Send password
    password.send_keys('ffH^v6^cB5B2t#aE')
    #Find login button
    login_button_found = False
    while login_button_found == False:
        try:
            #login_button = driver.find_element(By.XPATH, '///*[@id="next"]')
            login_button = driver.find_element(By.ID, 'next')
            login_button_found = True
            print("Login button found!")
        except:
            time.sleep(3)
            print("Couldn't find login button! Pausing for 3 seconds.")
    time.sleep(2)
    #Press login button
    login_button.click()
    time.sleep(2)
    #Find cookies button
    #onetrust-accept-btn-handler
    cookie_button_found = False
    while cookie_button_found == False:
        try:
            cookie_button = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
            cookie_button_found = True
            print("Cookie button found!")
        except:
            time.sleep(3)
            print("Couldn't find cookie button! Pausing for 3 seconds.")
    cookie_button.click()
    return driver

def check_for_tickets(driver):
    #Check if list_ticket_items exists - where tickets are held.
    try:
        ticket_list = driver.find_element(By.ID, 'list_ticket_items')
    except:
        print("No ticket items found!")
        return False
    #Get element table
    ticket_elements = ticket_list.find_elements(By.CLASS_NAME, 'group_start')
    #Check each element to see if adult ticket.
    for element in ticket_elements:
        print("About to process")
        if 'Adult' not in element.text:
            continue
        add_to_cart_button = element.find_element(By.CLASS_NAME, 'button')
        add_to_cart_button.click()
        buy_button = driver.find_element(By.XPATH, '//*[@id="book"]')
        buy_button.click()
        if input('Close?') != 'n':
            SystemExit.code(0)
            return True
    return False

def refresh_page(driver):
    driver.refresh()