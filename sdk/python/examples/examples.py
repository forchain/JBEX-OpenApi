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

    proxies = {
        "http": "",
        "https": "",
    }

    entry_point = 'https://api.jbex.com/openapi/'  # like: https://api.xxx.yyy/openapi/ where xxx.yyy is your base domain
    b = BrokerClient(entry_point, api_key='fzFNJk1qnDtw0RS3ERO9fDreqT6NjatM5obhRcETqK5xsJppzM3y9WHQndDaEpV2', secret='O4GDKZj5AFOT4PzXTnmdXWE1fnZlwdjOfgXzuBcNCjEWFryvncDlcZEAHlEz3g6S', proxies=proxies)

    # b.time()time

    # print(int(time.time() * 1000))

    broker_info = b.broker_info()

    # b.depth('MEERUSDT')

    # b.trades('MEERUSDT')

    # kl = b.klines('MEERUSDT', interval='1h')
    #
    # df = pd.DataFrame(kl)


    # b.ticker_24hr('MEERUSDT')

    # result = b.order_new(symbol='MEERUSDT', side='BUY', type='LIMIT', quantity='10', price='0.1', timeInForce='GTC')
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
