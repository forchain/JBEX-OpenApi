import unittest
import pandas as pd
import json
from datetime import datetime
import ast


# [
#   [
#     1499040000000,      // 开盘时间
#     "0.01634790",       // 开盘价
#     "0.80000000",       // 最高价
#     "0.01575800",       // 最低价
#     "0.01577100",       // 收盘价
#     "148976.11427815",  // 交易量
#     1499644799999,      // 收盘时间
#     "2434.19055334",    // Quote asset数量
#     308,                // 交易次数
#     "1756.87402397",    // Taker buy base asset数量
#     "28.46694368"       // Taker buy quote asset数量
#   ]
# ]

class JsonTestCase(unittest.TestCase):
    def test_save_file(self):
        raw = "[[1650506400000, '0.478', '0.491', '0.477', '0.479', '4068.967', 0, '1973.774051', 36, '0', '0'], [1650510000000, '0.479', '0.491', '0.478', '0.48', '1438.76', 0, '697.79846', 21, '0', '0']]"
        kline = ast.literal_eval(raw)
        df = pd.DataFrame(kline)
        df = df.set_axis(
            ['开盘时间', '开盘价', '最高价', '最低价', '收盘价', '交易量', '收盘时间', 'Quote asset数量', '交易次数', 'Taker buy base asset数量', 'Taker buy quote asset数量'],
            axis=1)
        print(df)

        df = df.drop(columns=['收盘时间', 'Quote asset数量', '交易次数', 'Taker buy base asset数量', 'Taker buy quote asset数量'])
        df['开盘时间'] = pd.to_datetime(df['开盘时间'], unit='ms')
        df = df.set_index('开盘时间')
        print(df)
        df.to_excel('klines.xlsx')
        # self.assertEqual(True, False)  # add assertion here

    def test_merge_data(self):
        d1 = "[[1650506400000, '0.478', '0.491', '0.477', '0.479', '4068.967', 0, '1973.774051', 36, '0', '0']]"
        d2 = "[[1650510000000, '0.479', '0.491', '0.478', '0.48', '1438.76', 0, '697.79846', 21, '0', '0']]"
        k1 = ast.literal_eval(d1)
        k2 = ast.literal_eval(d2)
        df1 = pd.DataFrame(k1)
        df2 = pd.DataFrame(k2)
        df = pd.concat([df1, df2])
        print(df)


    def test_to_excel(self):
        # importing packages
        import pandas as pd

        # dictionary of data
        dct = {'ID': {0: 23, 1: 43, 2: 12,
                      3: 13, 4: 67, 5: 89,
                      6: 90, 7: 56, 8: 34},
               'Name': {0: 'Ram', 1: 'Deep',
                        2: 'Yash', 3: 'Aman',
                        4: 'Arjun', 5: 'Aditya',
                        6: 'Divya', 7: 'Chalsea',
                        8: 'Akash'},
               'Marks': {0: 89, 1: 97, 2: 45, 3: 78,
                         4: 56, 5: 76, 6: 100, 7: 87,
                         8: 81},
               'Grade': {0: 'B', 1: 'A', 2: 'F', 3: 'C',
                         4: 'E', 5: 'C', 6: 'A', 7: 'B',
                         8: 'B'}
               }

        # forming dataframe
        data = pd.DataFrame(dct)

        # storing into the excel file
        data.to_excel("output.xlsx")


if __name__ == '__main__':
    unittest.main()
