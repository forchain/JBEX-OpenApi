import logging
import numpy as np
import pandas as pd

import sys
sys.path.insert(0, '..')
from broker.client import BrokerClient

if __name__ == '__main__':
    from broker import broker_log

    broker_log.setLevel(logging.DEBUG)
    broker_log.addHandler(logging.StreamHandler())

    entry_point = 'https://api.jbex.com/openapi/'  # like: https://api.xxx.yyy/openapi/ where xxx.yyy is your base domain
    b = BrokerClient(entry_point, api_key='', secret='')

    # b.time()time

    # print(int(time.time() * 1000))

    broker_info = b.broker_info()

    # b.depth('BTCUSDT')

    # b.trades('BTCUSDT')

    # kl = b.klines('BTCUSDT', interval='1h')
    #
    # df = pd.DataFrame(kl)


    # b.ticker_24hr('BTCUSDT')

    # result = b.order_new(symbol='BTCUSDT', side='BUY', type='LIMIT', quantity='10', price='0.1', timeInForce='GTC')
    #
    # print(result)
    #
    # order_id = result['orderId']
    #
    # print(order_id)
    #
    # print(b.order_get(order_id=order_id))
    #
    # print(b.order_cancel(order_id=order_id))
    #
    # print(b.open_orders())
    #
    # print(b.history_orders())
    #
    # print(b.account())
    #
    # print(b.my_trades())
    #
    # listen_key = b.stream_get_listen_key()
    #
    # print(listen_key)
    #
    # print(b.stream_keepalive(listen_key.get('listenKey')))
    #
    # print(b.stream_close(listen_key.get('listenKey')))
    #
    # print(b.deposit_orders())
