import time

from selenium import webdriver

link = input("[TikTok Views] Введите ссылку на видео: ")
arguments = ["--incognito", "--disable-blink-features", "--disable-blink-features=AutomationControlled",
             "--disable-plugins-discovery",
             "--disable-extensions", "--profile-directory=Default", "--start-maximized"]
views_count = 0


def driver_settings():
    options = webdriver.ChromeOptions()
    for argument in arguments:
        options.add_argument(argument)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    start(driver)


def start(driver):
    global views_count

    driver.get('https://zefoy.com/')
    x = 0
    z = 0
    while x != 1:
        try:
            driver.find_element_by_xpath('//*[@id="main"]/form/div/div/img')
            if z == 0:
                print("[TikTok Views] На сайте появилась капча. Введите её.")
                z += 1
        except Exception as error:
            x = 1
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/button').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="sid4"]/div/div/div/form/div/input').send_keys(link)
    time.sleep(0.3)
    driver.find_element_by_xpath('//*[@id="sid4"]/div/div/div/form/div/div/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/div[1]/div/form/button').click()
    while True:
        views_count += 1000
        print("[TikTok Views] ~+1,000 просмотров было накручено!\n"
              f"[TikTok Views] Вы уже накрутили {views_count:,d} просмотров.")
        print("[TikTok Views] Ожидание сайта...")
        time.sleep(358)
        driver.find_element_by_xpath('//*[@id="sid4"]/div/div/div/form/div/div/button').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/div[1]/div/form/button').click()
        time.sleep(2)


driver_settings()
