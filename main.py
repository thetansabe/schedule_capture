from selenium import webdriver
#from selenium.webdriver.common.keys import Keys #Keys.enter -> search bar
from selenium.webdriver.support.ui import Select
#from bs4 import BeautifulSoup

from datetime import datetime as dt
from time import sleep

def getWeekDates(driver):
    
    #select input chua thong tin khoang thoi gian cua tuan
    date_input = driver.find_element('id', 'ThoiKhoaBieu1_btnTuanHienTai')
    date_input_value = date_input.get_attribute('value')

    #print(date_input_value): 04/07/2022 - 10/07/2022
    from_to = date_input_value.split('-')
    from_date = from_to[0].strip()
    to_date = from_to[1].strip()

    return {from_date : from_date, to_date : to_date}

def takeScreenShot(driver, SAVE_PATH):
    ###take a real nice picture

    #open web in full view
    driver.maximize_window()

    #go to positon document.getElementById("ThoiKhoaBieu1_tbTKBTheoTuan").scrollIntoView()
    driver.execute_script('document.getElementById("ThoiKhoaBieu1_tbTKBTheoTuan").scrollIntoView()')

    #take screenshot
    driver.save_screenshot(SAVE_PATH)

def mainFunction(username='', password='', semesterCode='', date='', save_path=''):
    USERNAME = username
    PASSWORD = password

    SEMESTER_CODE = semesterCode
    DATE_LOOK_UP = date

    SAVE_PATH = save_path

    #Step 1: Login to std tdtu

    #open website
    driver = webdriver.Chrome()
    url = 'https://stdportal.tdtu.edu.vn/'
    driver.get(url)

    #login website
    user_field = driver.find_element('name','email')
    user_field.send_keys(USERNAME)

    password_field = driver.find_element('name','password')
    password_field.send_keys(PASSWORD)

    #click login
    sleep(1)
    login_btn = driver.find_element('id', 'btnLogIn')
    login_btn.click()

    #mo muc dao tao / old website
    sleep(1)
    schedule_url = 'https://lichhoc-lichthi.tdtu.edu.vn'
    driver.get(schedule_url)

    
    #vao hoc ki can crawl
    select_field = driver.find_element('id', 'ThoiKhoaBieu1_cboHocKy')
    dropdown = Select(select_field)

    dropdown.select_by_value(SEMESTER_CODE)

    flag = True #start looping

    while flag:
        from_date , to_date = getWeekDates(driver)

        #xu li string date -> datetime
        from_date = dt.strptime(from_date, "%d/%m/%Y")
        to_date = dt.strptime(to_date, "%d/%m/%Y")
        my_date = dt.strptime(DATE_LOOK_UP, "%d/%m/%Y")

        if(my_date >= from_date and my_date <= to_date): 
            takeScreenShot(driver, SAVE_PATH)
            flag = False
        else:
            #xu li chuyen trang
            next_btn = driver.find_element('id', 'ThoiKhoaBieu1_btnTuanSau')
            next_btn.click()

    return True