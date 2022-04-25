from datetime import datetime, timedelta

import time
import unittest
import logging

from broker.client import BrokerClient
from broker import broker_log
import pandas as pd


class TraderTestCase(unittest.TestCase):
    def test_server_time(self):
        broker_log.setLevel(logging.DEBUG)
        broker_log.addHandler(logging.StreamHandler())

        proxies = {
            "http": "",
            "https": "",
        }

        entry_point = 'https://api.jbex.com/openapi/'  # like: https://api.xxx.yyy/openapi/ where xxx.yyy is     your base domain
        self.broker_client = BrokerClient(entry_point,
                                          api_key='',
                                          secret='',
                                          proxies=proxies)
        t = self.broker_client.time()
        print(t)

    def test_first_kline(self):
        # 0.1,1.5,0.1,1.32
        # start_date = '2021-10-28'

        sd = datetime(year=2021, month=11, day=30)
        print(sd)
        ed = sd + timedelta(days=1)
        print(ed)
        st = int(datetime.timestamp(sd) * 1000)
        et = int(datetime.timestamp(ed) * 1000)

        print(st)
        print(et)

        broker_log.setLevel(logging.DEBUG)
        broker_log.addHandler(logging.StreamHandler())

        proxies = {
            "http": "",
            "https": "",
        }

        entry_point = 'https://api.jbex.com/openapi/'  # like: https://api.xxx.yyy/openapi/ where xxx.yyy is your base domain
        b = BrokerClient(entry_point, api_key='',
                         secret='', proxies=proxies)

        raw = b.klines('BTCUSDT', interval='1h', limit=1000, start_time=st, end_time=et)
        df = pd.DataFrame(raw)
        print(df)
        self.assertTrue(True)

    def test_consecutive_klines(self):
        # 0.1,1.5,0.1,1.32
        # start_date = '2021-10-28'

        broker_log.setLevel(logging.DEBUG)
        broker_log.addHandler(logging.StreamHandler())

        proxies = {
            "http": "",
            "https": "",
        }

        entry_point = 'https://api.jbex.com/openapi/'  # like: https://api.xxx.yyy/openapi/ where xxx.yyy is your base domain
        b = BrokerClient(entry_point, api_key='',
                         secret='O4GDKZj5AFOT4PzXTnmdXWE1fnZlwdjOfgXzuBcNCjEWFryvncDlcZEAHlEz3g6S', proxies=proxies)

        sd = datetime(year=2021, month=12, day=1)
        print(sd)
        ed = sd + timedelta(days=1)
        print(ed)
        st = int(datetime.timestamp(sd) * 1000)
        et = int(datetime.timestamp(ed) * 1000)

        print(st)
        print(et)
        raw = b.klines('BTCUSDT', interval='1h', start_time=st, end_time=et)
        df = pd.DataFrame(raw)
        print(df)

        sd = ed + timedelta(hours=1)
        print(sd)
        ed = sd + timedelta(days=1)
        print(ed)
        st = int(datetime.timestamp(sd) * 1000)
        et = int(datetime.timestamp(ed) * 1000)

        print(st)
        print(et)
        raw = b.klines('BTCUSDT', interval='1h', start_time=st, end_time=et)
        df = pd.DataFrame(raw)
        print(df)

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
