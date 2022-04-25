import logging
import time

import numpy as np
from datetime import datetime, timedelta
import pandas as pd
from broker import broker_log

import sys

sys.path.insert(0, '..')
from broker.client import BrokerClient


class JubiTrader:
    def __init__(self, year=2021, month=12, day=1, pair='MEERUSDT', days=0):
        self.start_date = datetime(year=year, month=month, day=day)
        self.pair = pair
        self.end_date = self.start_date + timedelta(days=days)

    def connect(self):
        broker_log.setLevel(logging.DEBUG)
        broker_log.addHandler(logging.StreamHandler())

        proxies = {
            "http": "",
            "https": "",
        }

        entry_point = 'https://api.jbex.com/openapi/'  # like: https://api.xxx.yyy/openapi/ where xxx.yyy is your base domain
        self.broker_client = BrokerClient(entry_point,
                                          api_key='fzFNJk1qnDtw0RS3ERO9fDreqT6NjatM5obhRcETqK5xsJppzM3y9WHQndDaEpV2',
                                          secret='O4GDKZj5AFOT4PzXTnmdXWE1fnZlwdjOfgXzuBcNCjEWFryvncDlcZEAHlEz3g6S',
                                          proxies=proxies)
        ts_now = time.time()
        if self.end_date == self.start_date:
            self.end_date = datetime.fromtimestamp(ts_now)

    def run(self):
        self.connect()

        start_date = self.start_date
        end_date = start_date + timedelta(days=1)
        print("start_date", start_date)
        print("end_date", end_date)
        df = pd.DataFrame()
        while end_date <= self.end_date:
            start_time = int(datetime.timestamp(start_date) * 1000)
            end_time = int(datetime.timestamp(end_date) * 1000)
            print("start_time", start_time)
            print("end_time", end_time)
            klines = self.broker_client.klines(self.pair, interval='1h', start_time=start_time, end_time=end_time)
            df_k = pd.DataFrame(klines)
            df_k = df_k.drop(df_k.columns[[6, 7, 8, 9, 10]], axis=1)
            df_k = df_k.set_axis(['time', 'open', 'high', 'low', 'close', 'amount'], axis=1)
            df_k['time'] = pd.to_datetime(df_k['time'], unit='ms')
            df_k = df_k.set_index('time')

            df = pd.concat([df, df_k])

            start_date = end_date + timedelta(hours=1)
            end_date = start_date + timedelta(days=1)
        print(df)
        df.to_excel('/tmp/klines.xlsx')


if __name__ == '__main__':
    jt = JubiTrader(days=0)
    jt.run()
