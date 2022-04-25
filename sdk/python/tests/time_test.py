import unittest
import time
from datetime import datetime, timedelta


class TimeTestCase(unittest.TestCase):
    def test_read_from_stamp(self):
        msec = 1638277200000
        sec = msec / 1000
        print("sec", sec)
        # self.assertEqual(True, False)  # add assertion ere
        st = time.gmtime(sec)
        print("st", st)

        mk = time.mktime(st)
        print("mk", mk)

        ct = time.ctime(sec)
        print("ct", ct)

        lt = time.localtime(sec)
        print("lt", lt)
        mlt = int(time.mktime(lt))
        print("mlt", mlt)

        self.assertEqual(sec, mlt)

        now = int(time.time() * 1000)
        print("now", now)



    def test_set_time(self):
        msec = 1650495600000
        sec = msec / 1000
        print("sec", sec)

        lt = time.localtime(sec)
        print("lt", lt)
        mlt = int(time.mktime(lt))
        print("mlt", mlt)
        self.assertTrue(True, "Done!")

    def test_date_time(self):
        dt = datetime(year=2021, month=1, day=28)
        print(dt)
        ts = datetime.timestamp(dt)
        print(ts)

        now = datetime.timestamp(datetime.now())
        print("timestamp", now)

        now = datetime.fromtimestamp(time.time())
        print("now", now)

    def test_add_date(self):
        dt = datetime(year=2021, month=1, day=28)

        print(dt)
        dt = dt + timedelta(days=1)
        print(dt)
        ts = datetime.timestamp(dt)
        print(ts)


if __name__ == '__main__':
    unittest.main()
