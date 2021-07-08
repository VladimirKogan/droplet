import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import time
from bot import main_func
from tg import send_message_to_bot
from datetime import datetime

base_url = sys.argv[1]
part = int(sys.argv[2])

# base_url = 'elonmusk'
# part = 2

X_PATH_PINNED_TEXT = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/section/div/div/div[1]/div/div/article/div/div/div/div/div/div/div/div/div[2]/div/div/div/span'
X_PATH_RETWEETED = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/section/div/div/div[1]/div/div/article/div/div/div/div/div/div/div/div/div[2]/div/div/div/a/span'


def get_tweet_text(driver, num):
    try:
        xPathText = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/section/div/div/div[' + str(num) + ']/div/div/article/div/div/div/div[2]/div[2]/div[2]/div/div/span'
        return driver.find_element_by_xpath(xPathText).text
    except:
        return 0


def get_tweet_image_path(driver, num):
    try:
        xPathImg = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[4]/div/div/section/div/div/div["+str(num)+"]/div/div/article/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/a/div/div[2]/div/img"
        return driver.find_element_by_xpath(xPathImg).get_attribute("src")
    except:
        return 0


def if_has_pinned_tweet(driver):
    try:
        pinned = driver.find_element_by_xpath(X_PATH_PINNED_TEXT)
        return 3
    except:
        return 1


def if_tweet_retweet(driver, num):
    try:
        retweet = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/section/div/div/div[" + str(num) + "]/div/div/article/div/div/div/div/div/div/div/div/div[2]/div/div/div/a/span")
        return 1
    except:
        return 0


def get_last_tweet(driver):
    last_tweet_num = if_has_pinned_tweet(driver)
    check_tweet_retweet = if_tweet_retweet(driver, last_tweet_num)
    if check_tweet_retweet == 0:
        if get_tweet_text(driver, last_tweet_num) != 0:
            return get_tweet_text(driver, last_tweet_num)
        elif get_tweet_text(driver, last_tweet_num) == 0 and get_tweet_image_path(driver, last_tweet_num) != 0:
            return get_tweet_image_path(driver, last_tweet_num)
        else:
            return "Nothing to do"
    else:
        return 1


def whait_page_to_load_and_get_last_tweet(driver):
    while True:
        try:
            last_tweet = get_last_tweet(driver)
            break
        except:
            time.sleep(0.1)
    return last_tweet


def check_if_page_is_loaded(driver):
    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/section/div/div/div[1]')
            break
        except:
            driver.wait = WebDriverWait(driver, 0.1)
    return 1


def createDriver():
    print("Start Creating Driver")
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--disable-infobars')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--remote-debugging-port=9222')
    # driver = webdriver.Chrome(options=options, executable_path='/Users/vladimirkogan/Downloads/chromedriver91') # LOCAL
    driver = webdriver.Chrome(options=options, executable_path='drivers/driver241/chromedriver') # DIGITAL OCEAN DROPLET
    return driver


def restartAll(driver, url):
    print('CLOSE DRIVER')
    driver.stop_client()
    driver.close()
    driver.quit()
    driverStart(url)


def driverStart(name):
    count = 0
    LAST_SAVED_TWEET = 'Nothing to do'
    start_time = time.time()
    url = "https://twitter.com/"+name
    driver = createDriver()
    try:
        driver.get(url)
        while True:
            if count >= 100:
                restartAll(driver, name)
            check_if_page_is_loaded(driver)
            last_tweet = get_last_tweet(driver)
            # print("LAST TWEET: " + str(last_tweet))
            count = count + 1
            done_time = time.time()
            print(f"Iteration: {count}, {last_tweet} in {done_time-start_time} LAST SAVED: {LAST_SAVED_TWEET}")
            start_time = done_time
            if LAST_SAVED_TWEET != 'Nothing to do' and LAST_SAVED_TWEET != last_tweet:
                LAST_SAVED_TWEET = last_tweet
                main_func(last_tweet)
            if LAST_SAVED_TWEET == 'Nothing to do':
                LAST_SAVED_TWEET = last_tweet
            driver.refresh()
    except:
        driver.stop_client()
        driver.close()
        driver.quit()
        driverStart(name)


driverStart(base_url)


