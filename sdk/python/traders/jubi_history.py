import logging
import time

import numpy as np
import json
from datetime import datetime, timedelta
import pandas as pd
from broker import broker_log

import sys

sys.path.insert(0, '..')
from broker.client import BrokerClient


class JubiTrader:
    def __init__(self):
        fp = open('config/config.json', 'r')
        self.config = json.load(fp)
        self.start_date = datetime(year=self.config["year"], month=self.config["month"], day=self.config["day"])
        self.pair = self.config["pair"]
        self.end_date = self.start_date + timedelta(days=self.config["days"])

    def connect(self):
        broker_log.setLevel(logging.DEBUG)
        broker_log.addHandler(logging.StreamHandler())

        proxies = {
            "http": "",
            "https": self.config["proxy"],
        }

        entry_point = 'https://api.jbex.com/openapi/'  # like: https://api.xxx.yyy/openapi/ where xxx.yyy is your base domain
        self.broker_client = BrokerClient(entry_point,
                                          api_key=self.config["api_key"],
                                          secret=self.config["secret"],
                                          proxies=proxies)
        ts_now = time.time()
        if self.end_date == self.start_date:
            self.end_date = datetime.fromtimestamp(ts_now)

    def run(self):
        self.connect()

        start_date = self.start_date
        # end_date = start_date + timedelta(days=1)
        end_date = start_date + timedelta(days=40)
        print("start_date", start_date)
        print("end_date", end_date)
        df = pd.DataFrame()
        while start_date <= self.end_date:
            start_time = int(datetime.timestamp(start_date) * 1000)
            end_time = int(datetime.timestamp(end_date) * 1000)
            print("start_time", start_time)
            print("end_time", end_time)
            klines = self.broker_client.klines(self.pair, interval='1h', start_time=start_time, end_time=end_time,
                                               limit=999)
            df_k = pd.DataFrame(klines)
            if df_k.empty:
                continue
            df_k = df_k.drop(df_k.columns[[6, 7, 8, 9, 10]], axis=1)
            df_k = df_k.set_axis(['time', 'open', 'high', 'low', 'close', 'amount'], axis=1)
            df_k['time'] = pd.to_datetime(df_k['time'], unit='ms')
            df_k = df_k.set_index('time')

            df = pd.concat([df, df_k])

            start_date = end_date + timedelta(hours=1)
            end_date = start_date + timedelta(days=40)
        print(df)
        df.to_excel('/tmp/jubi-history.xlsx')


if __name__ == '__main__':
    jt = JubiTrader()
    jt.run()
