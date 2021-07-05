import requests
import re
from tg import send_message_to_bot

REGEX = r"\b[A-Z0-9][A-Z0-9]+\b"
TRIGGER_TEXT = "inbound transfer"
COINSPAIR = {'SUSHIUSDT': 50, 'CVCUSDT': 50, 'BTSUSDT': 50, 'HOTUSDT': 50, 'ZRXUSDT': 50, 'QTUMUSDT': 50,
             'IOTAUSDT': 50, 'BTCBUSD': 50, 'WAVESUSDT': 50, 'ADAUSDT': 75, 'LITUSDT': 50, 'XTZUSDT': 75,
             'BNBUSDT': 75, 'AKROUSDT': 50, 'HNTUSDT': 50, 'ETCUSDT': 75, 'XMRUSDT': 75, 'YFIUSDT': 50, 'ETHUSDT': 100,
             'ALICEUSDT': 50, 'ALPHAUSDT': 50, 'SFPUSDT': 50, 'REEFUSDT': 50, 'BATUSDT': 50, 'DOGEUSDT': 50,
             'RLCUSDT': 50, 'TRXUSDT': 75, 'STORJUSDT': 50, 'SNXUSDT': 50, 'ETHUSDT_210625': 25, 'XLMUSDT': 75,
             'NEOUSDT': 50, 'UNFIUSDT': 50, 'SANDUSDT': 50, 'DASHUSDT': 50, 'KAVAUSDT': 50, 'RUNEUSDT': 50,
             'CTKUSDT': 50, 'LINKUSDT': 75, 'CELRUSDT': 50, 'RSRUSDT': 50, 'DGBUSDT': 25, 'SKLUSDT': 50, 'RENUSDT': 50,
             'TOMOUSDT': 50, 'MTLUSDT': 50, 'LTCUSDT': 75, 'DODOUSDT': 50, 'KSMUSDT': 50, 'EGLDUSDT': 50,
             'BTCUSDT_210625': 25, 'VETUSDT': 50, 'ONTUSDT': 50, 'TRBUSDT': 50, 'MANAUSDT': 50, 'COTIUSDT': 50,
             'CHRUSDT': 50, 'BAKEUSDT': 25, 'GRTUSDT': 50, 'FLMUSDT': 50, 'EOSUSDT': 75, 'OGNUSDT': 50, 'SCUSDT': 25,
             'BALUSDT': 50, 'STMXUSDT': 50, 'BTTUSDT': 50, 'LUNAUSDT': 50, 'DENTUSDT': 50, 'KNCUSDT': 50,
             'SRMUSDT': 50, 'ENJUSDT': 50, 'ZENUSDT': 50, 'ATOMUSDT': 50, 'NEARUSDT': 50, 'BCHUSDT': 75,
             'IOSTUSDT': 50, 'HBARUSDT': 50, 'ZECUSDT': 50, '1000SHIBUSDT': 25, 'BZRXUSDT': 50, 'AAVEUSDT': 50,
             'ALGOUSDT': 50, 'ICPUSDT': 25, 'LRCUSDT': 50, 'AVAXUSDT': 50, 'MATICUSDT': 50, '1INCHUSDT': 50,
             'MKRUSDT': 50, 'THETAUSDT': 50, 'UNIUSDT': 50, 'LINAUSDT': 50, 'RVNUSDT': 50, 'FILUSDT': 50, 'NKNUSDT': 25,
             'DEFIUSDT': 50, 'COMPUSDT': 50, 'SOLUSDT': 50, 'BTCUSDT': 125, 'OMGUSDT': 50, 'ICXUSDT': 50, 'BLZUSDT': 50,
             'FTMUSDT': 50, 'YFIIUSDT': 50, 'BANDUSDT': 50, 'XRPUSDT': 75, 'SXPUSDT': 50, 'CRVUSDT': 50, 'BELUSDT': 50,
             'DOTUSDT': 75, 'XEMUSDT': 50, 'ONEUSDT': 50, 'ZILUSDT': 50, 'AXSUSDT': 50, 'OCEANUSDT': 50, 'CHZUSDT': 50,
             'ANKRUSDT': 50}

def from_tweet_return_array_of_coins(tweet):
    arr = tweet.split()
    pairs = []
    for t in arr:
        word = re.sub('[\W_]+', '', t).upper()
        if word in COINSPAIR or word + "USDT" in COINSPAIR:
            if word in COINSPAIR and word not in pairs:
                pairs.append(word)
            elif word + "USDT" in COINSPAIR and word + "USDT" not in pairs:
                pairs.append(word + "USDT")
    print(f"TWEET: {tweet}\n\nPAIRS: {pairs}")
    return pairs


def callOutsideRobotLeverageSum(pair, time, sum, leverage, action):
    # address = 'http://localhost:3344'
    address = 'https://binance-worker-eqw8s.ondigitalocean.app' # Vladimir
    url = address + '/?coin=' + pair + '&sleep_time=' + str(time) + '&sum='+str(sum) + '&action=' + action + '&leverage='+str(leverage)
    print(url)
    try:
        requests.get(url, timeout=1)
    except:
        return



def from_tweet_return_dict_of_coins(tweet):
    arr = tweet.split()
    pairs = {}
    for t in arr:
        word = re.sub('[\W_]+', '', t).upper()
        if word in COINSPAIR or word + "USDT" in COINSPAIR:
            if word in COINSPAIR and word not in pairs:
                pairs[word] = COINSPAIR[word]
            elif word + "USDT" in COINSPAIR and word + "USDT" not in pairs:
                pairs[word + "USDT"] = COINSPAIR[word + "USDT"]
    print(f"TWEET: {tweet}\n\nPAIRS: {pairs}")
    return pairs


def main_func(tweet):
    if "doge" in tweet.lower():
         callOutsideRobotLeverageSum("DOGEUSDT", 50, 30, COINSPAIR["DOGEUSDT"], 'buy_wait_sell')
         send_message_to_bot(f"SIGNAL TWEET: \n\n{tweet}")
    elif "shib" in tweet.lower():
        callOutsideRobotLeverageSum("1000SHIBUSDT", 50, 30, COINSPAIR["1000SHIBUSDT"], 'buy_wait_sell')
    elif "test" in tweet.lower():
        pairs=from_tweet_return_dict_of_coins(tweet.lower())
        for p in pairs:
            callOutsideRobotLeverageSum(p, 50, 20, pairs[p], 'buy_wait_sell_test')
    else:
        send_message_to_bot(f"JUST A TWEET: \n\n{tweet}")
