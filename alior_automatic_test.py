import traceback
from selenium import webdriver
import time

data_set = {
    'name': 'Albert',
    'lastname': 'Tokarski',
    'mail': 'albert.tokarski_rekrutacja@mymail.com',
    'phone_number': '606409506',
    'cash_amount': '500'}

url = 'https://wnioski.aliorbank.pl/spinner-process/?partnerId=POR_P_ZERO_S&transactionCode=pozyczki'
my_executable_path = '/Users/albert/Documents/TestFiles/chromedriver'

driver = webdriver.Chrome(executable_path=my_executable_path)
driver.get(url)
driver.maximize_window()
time.sleep(2)

try:
    assert driver.title == "Alior Bank"
    driver.find_element_by_xpath(".//*[contains(text(), 'Zamknij')]").click()
    driver.find_element_by_id('firstName').send_keys(data_set.get("name"))
    driver.find_element_by_id('lastName').send_keys(data_set.get("lastname"))
    driver.find_element_by_id('emailAddress').send_keys(data_set.get("mail"))
    driver.find_element_by_id('mobileNumber mobileNumber').send_keys('000000000')
    cashAmount = driver.find_element_by_id('cashAmount cashAmount').send_keys(data_set.get("cash_amount"))

    driver.find_element_by_id('installmentYears').click()
    driver.find_element_by_xpath('//*[@id="installmentYears"]/div/span/div/div[2]/div/div[2]').click()

    driver.find_element_by_id('installmentMonths').click()
    driver.find_element_by_xpath('//*[@id="installmentMonths"]/div/span/div/div[2]/div/div[11]').click()

    driver.find_element_by_xpath(".//*[contains(text(), 'informacyjne')]").click()
    driver.find_element_by_xpath(".//*[contains(text(), 'przez Bank')]").click()
    driver.find_element_by_xpath(".//*[contains(text(), 'przez BIK')]").click()

    driver.find_element_by_xpath(".//*[contains(text(), 'Dalej')]").click()

    phone_error_messages = driver.find_elements_by_xpath(".//*[contains(text(), 'Niepoprawny numer telefonu')]")
    if len(phone_error_messages) > 0:
        driver.find_element_by_id('mobileNumber mobileNumber').clear()
        driver.find_element_by_id('mobileNumber mobileNumber').send_keys(data_set.get("phone_number"))

except AssertionError:
    print("***ERROR***\n" + traceback.format_exc())
# finally:
    # driver.close()
