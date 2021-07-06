import sys
from selenium import webdriver
import time
from bot import main_func
from tg import send_message_to_bot
from datetime import datetime

base_url=sys.argv[1]
part = int(sys.argv[2])

FIRST_TWEET_XML = "(//div[@lang='en'])[1]/span"
SECOND_TWEET_XML = "(//div[@lang='en'])[2]/span"

xPathPinnedText = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/section/div/div/div[1]/div/div/article/div/div/div/div/div/div/div/div/div[2]/div/div/div/span'
xPathRetweeted = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/section/div/div/div[1]/div/div/article/div/div/div/div/div/div/div/div/div[2]/div/div/div/a/span'
ELON_MUSK_TWITTER = "https://twitter.com/elonmusk"
VLADIK = "https://twitter.com/Vladik01752005"


def getTweetByNum(driver, num):
    if if_tweet_retweet(driver, num) == 0:
        xPathTweetsIfPinned = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/section/div/div/div[' + str(num) + ']/div/div/article/div/div/div/div[2]/div[2]/div[2]/div/div/span'
        return driver.find_element_by_xpath(xPathTweetsIfPinned).text
    else:
        return "retweeted"


def if_has_pinned_tweet(driver):
    try:
        pinned = driver.find_element_by_xpath(xPathPinnedText)
        return 3
    except:
        return 1


def check_minute(minute):
    m = int(minute)
    first = [0, 1, 2, 3, 4]
    second = [5, 6, 7, 8, 9]
    third = [10, 11, 12, 13, 14]

    if m % 15 in first: return 1
    if m % 15 in second: return 2
    if m % 15 in third: return 3
    return 0


def check_time():
    while True:
        break
        minutes = datetime.now().strftime("%M")
        if check_minute(minutes) == part:
            break
        print("sleep")
        time.sleep(1)


def if_tweet_retweet(driver, num):
    try:
        retweet = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/section/div/div/div["+str(num)+"]/div/div/article/div/div/div/div/div/div/div/div/div[2]/div/div/div/a/span")
        return 1
    except:
        return 0

def driverStart(name):
    counter = 1
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--incognito')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-debugging-port=9222')
    driver = webdriver.Chrome(options=options, executable_path='drivers/driver241/chromedriver')
    driver.get(base_url)
    LAST_TWEET = ''
    while True:
        check_time()
        while True:
            try:
                last_tweet = getTweetByNum(driver, 1)
                break
            except:
                time.sleep(0.01)
        current_time = datetime.now().strftime("%H:%M:%S")
        first_tweet_num = if_has_pinned_tweet(driver)
        last_tweet = getTweetByNum(driver, first_tweet_num)
        print(f"Current Time ({counter})=, {str(current_time)}: {last_tweet}")
        counter += 1
        if LAST_TWEET == '':
            LAST_TWEET = last_tweet
        elif LAST_TWEET != last_tweet and last_tweet != 'retweeted':
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)
            main_func(last_tweet)
            send_message_to_bot("TWITTERPARSE: " + last_tweet)
            new_tweet = last_tweet
            LAST_TWEET = new_tweet

        driver.refresh()
driverStart(base_url)
