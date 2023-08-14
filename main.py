import time

from selenium import webdriver
import random
import Selenium

def main():
    #Open web page
    driver = Selenium.open_page()
    #See if tix are available for adult
    tickets_found = False
    while tickets_found == False:
        result = Selenium.check_for_tickets(driver)
        if result == False:
            pause_interval = random.randrange(2,5)
            print("No tickets found, pausing for " + pause_interval.__str__() + " seconds.")
            time.sleep((pause_interval))
            Selenium.refresh_page(driver)
        else:
            tickets_found == True

if __name__ == "__main__":
    main()