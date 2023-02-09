#!/usr/bin/python3
import RPi.GPIO as GPIO
import dht11
import time
import logging
import datetime


# init
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin=14)

# ロギング設定
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 出力先を'./temp.log'に指定
handler = logging.FileHandler('./temp.log')
handler.setLevel(logging.INFO)

while True:
    result = instance.read()
    if result.is_valid():

        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        formatter = logging.Formatter(date + ' %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # ログファイルに出力
        logger.info(str(result.temperature) + ',' + str(result.humidity))

    time.sleep(60)  # 実行頻度（1分一回実行）
